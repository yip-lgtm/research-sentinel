#!/usr/bin/env python3
"""人性化練習哨兵 — 確定性 Telegram 投遞器（不依賴 LLM）

存在的理由（2026-11-01~04 實測事故）：
  cron 個 LLM 步驟撞 Token Plan 429 → cron Response 變成錯誤字串 → 用戶只收到
  「API call failed」而唔係報告。但報告本身有時已經喺磁碟寫好、過咗品質閘、
  commit 咗。finalize.py 補到 index，但 Telegram 投遞仍然死咗（finalize.py 個
  send_to_channel() 係死碼）。

  呢個模組補上最後一格：磁碟有過閘報告 → 產生投遞版 → MarkdownV2 轉換 →
  直接送 Telegram → 記低投遞狀態（冪等，唔會重複發）。

用法：
  python3 deliver.py --report reports/2026-11-03-21.md
  python3 deliver.py --stamp 2026-11-03-21
  python3 deliver.py --list               # 睇投遞狀態

⚠️ 刻意冇 --rescue-missing 全量掃描（2026-11-05 實測教訓）：
  index.json 入面 60+ 份舊報告嘅 delivered_utc 都係 None，但嗰啲報告實際上
  由 gateway 正常投遞咗（cron Response → Telegram）。ledger 只記錄 deliver.py
  自己送過嘅，所以全量掃描會令用戶一次過收到幾十份舊報告。
  補投遞只可以精準打一個 stamp（finalize.py 喺「Response 係錯誤字串」分支
  呼叫 --stamp），唔可以全量。

投遞版一律用 quality_gate.py --delivery 產生（≤3900 chars），唔可以直接貼
存檔版 —— gateway 只保留 3800 chars，貼長版用戶只見尾部（用戶投訴過）。
"""
import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HERMES_HOME", "/root/.hermes"))
REPO = HERMES_HOME / "sentinel"
REPORTS = REPO / "reports"
INDEX = REPORTS / "index.json"
GATE = REPO / "quality_gate.py"
LEDGER = REPORTS / "delivery.json"
API = "https://api.telegram.org/bot{token}/{method}"


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} deliver: {msg}", flush=True)


def load_env() -> None:
    """由 /root/.hermes/.env 載入 TELEGRAM_BOT_TOKEN。

    2026-11-05 實測 bug：keepalive 由 supervisord  起，環境只有 HERMES_HOME
    同 PATH，冇 TELEGRAM_BOT_TOKEN → telegram_send() 直接 RuntimeError，
    補投遞永遠失敗。token 其實喺 /root/.hermes/.env，要自己讀。
    """
    env_file = HERMES_HOME / ".env"
    if not env_file.exists():
        return
    try:
        for line in env_file.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            if k and v and not os.environ.get(k):
                os.environ[k] = v
    except Exception as exc:  # noqa: BLE001
        log(f"讀 .env 失敗（{type(exc).__name__}: {exc}）")


def load_ledger() -> dict:
    if LEDGER.exists():
        try:
            return json.loads(LEDGER.read_text())
        except Exception:
            pass
    return {"delivered": {}, "updated_utc": None}


def save_ledger(led: dict) -> None:
    led["updated_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text(json.dumps(led, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def run_gate(path: Path) -> dict:
    r = subprocess.run([sys.executable, str(GATE), str(path), "--json"],
                       cwd=str(REPO), capture_output=True, text=True, timeout=120)
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"pass": False, "fails": ["gate json parse fail"]}


def make_delivery(path: Path) -> str:
    """由存檔版生成投遞版（≤3900 chars，英文正文移除）。"""
    r = subprocess.run([sys.executable, str(GATE), str(path), "--delivery"],
                       cwd=str(REPO), capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError(f"quality_gate --delivery rc={r.returncode}: {r.stderr[:200]}")
    return r.stdout.rstrip("\n")


def to_mdv2(text: str) -> str:
    """Markdown → MarkdownV2。優先複用 gateway 自己嘅轉換器，確保同正常投遞一致。"""
    try:
        from gateway.platforms.telegram import TelegramAdapter
        return TelegramAdapter.format_message(None, text)
    except Exception as exc:  # noqa: BLE001
        log(f"用 gateway format_message 失敗（{type(exc).__name__}: {exc}），改用保守 escape")
        import re
        return re.sub(r"([_*\[\]()~`>#\+\-=|{}.!\\])", r"\\\1", text)


def telegram_send(text: str, chat_id: str, dry_run: bool = False) -> dict:
    load_env()
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN 未設定（.env 都搵唔到）")
    if dry_run:
        return {"ok": True, "dry_run": True, "chars": len(text)}
    import requests
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "MarkdownV2",
        "disable_web_page_preview": True,
    }
    r = requests.post(API.format(token=token, method="sendMessage"),
                      json=payload, timeout=45)
    try:
        body = r.json()
    except Exception:
        body = {"ok": False, "description": r.text[:200]}
    if not body.get("ok"):
        # MarkdownV2 解析失敗 → 退回純文字再試一次（寧可格式差過完全唔送）
        log(f"MarkdownV2 送出失敗（{body.get('description')}），改用純文字重試")
        r2 = requests.post(API.format(token=token, method="sendMessage"),
                           json={"chat_id": chat_id, "text": text,
                                 "disable_web_page_preview": True},
                           timeout=45)
        try:
            body2 = r2.json()
        except Exception:
            body2 = {"ok": False, "description": r2.text[:200]}
        body2["fallback_plain"] = True
        body2["chars"] = len(text)
        return body2
    body["chars"] = len(text)
    return body


def deliver_stamp(stamp: str, chat_id: str, force: bool = False, dry_run: bool = False) -> dict:
    path = REPORTS / f"{stamp}.md"
    if not path.exists():
        path = REPORTS / "archive" / f"{stamp}.md"
    if not path.exists():
        return {"ok": False, "reason": "磁碟冇報告檔"}

    gate = run_gate(path)
    if not gate.get("pass"):
        return {"ok": False, "reason": f"品質閘 FAIL: {gate.get('fails')}"}

    led = load_ledger()
    rec = led["delivered"].get(stamp, {})
    if rec.get("ok") and not force:
        return {"ok": True, "reason": "已投遞過（冪等跳過）", "stamp": stamp,
                "delivered_utc": rec.get("delivered_utc")}

    # 第二重冪等：index.json 嘅 delivered_utc 都係投遞證據。
    # 2026-11-05 實測：2026-10-29-22 index 有 delivered_utc 但 ledger 冇
    # （當時用 deliver.py 送過但 ledger 格式未更新），單靠 ledger 會重複發。
    if not force:
        idx_rec = index_entry(stamp)
        if idx_rec.get("delivered_utc"):
            return {"ok": True, "reason": "index 已記錄投遞（冪等跳過）", "stamp": stamp,
                    "delivered_utc": idx_rec.get("delivered_utc")}

    delivery = make_delivery(path)
    if len(delivery) > 3900:
        return {"ok": False, "reason": f"投遞版 {len(delivery)} chars > 3900"}
    mdv2 = to_mdv2(delivery)
    res = telegram_send(mdv2, chat_id, dry_run=dry_run)
    if not res.get("ok"):
        return {"ok": False, "reason": f"telegram 失敗: {res.get('description')}", "stamp": stamp}

    if dry_run:
        log(f"[dry-run] {stamp} 會投遞 {len(delivery)} chars（冇真送，冇寫 ledger）")
        return {"ok": True, "stamp": stamp, "chars": len(delivery), "dry_run": True}

    led["delivered"][stamp] = {
        "ok": True,
        "chars": len(delivery),
        "mdv2_chars": len(mdv2),
        "delivered_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "chat_id": chat_id,
        "dry_run": bool(dry_run),
        "source_file": str(path),
        "fallback_plain": bool(res.get("fallback_plain")),
    }
    save_index_delivery(stamp, led["delivered"][stamp])
    save_ledger(led)
    log(f"已投遞 {stamp}（{len(delivery)} chars，chat={chat_id}）")
    return {"ok": True, "stamp": stamp, "chars": len(delivery)}


def index_entry(stamp: str) -> dict:
    """讀 index.json 入面某個報告嘅條目（讀唔到就回空 dict）。"""
    if not INDEX.exists():
        return {}
    try:
        idx = json.loads(INDEX.read_text())
    except Exception:
        return {}
    return idx.get("reports", {}).get(stamp, {}) or {}


def save_index_delivery(stamp: str, rec: dict) -> None:
    """喺 index.json 記低投遞時間，方便網站顯示。"""
    if not INDEX.exists():
        return
    try:
        idx = json.loads(INDEX.read_text())
    except Exception:
        return
    entry = idx.get("reports", {}).get(stamp)
    if entry is None:
        return
    entry["delivered_utc"] = rec.get("delivered_utc")
    entry["delivery_chars"] = rec.get("chars")
    idx["updated_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def rescue_missing(chat_id: str, force: bool = False, dry_run: bool = False) -> list:
    """補投遞「過咗閘但從未送到 Telegram」嘅報告。

    ⚠️ 2026-11-05：呢個全量掃描已被刻意廢棄（只保留 --rescue-missing 作
    人工／一次性用途，唔會喺自動化流程裡面行）。

    原因：index.json 入面 60+ 份舊報告嘅 delivered_utc 都係 None，但嗰啲報告
    實際上係由 gateway 正常投遞咗（cron Response → Telegram）。delivery.json
    ledger 只記錄 deliver.py 自己送過嘅，所以用 ledger 做「未投遞」判據會
    造成大量重複投遞。

    自動化流程只會精準打一個 stamp（--stamp），由 finalize.py 喺「Response 係
    錯誤字串」嗰個分支觸發。
    """
    led = load_ledger()
    out = []
    candidates = sorted(
        p for p in REPORTS.glob("*.md")
        if p.name != "index.md" and not p.name.startswith("_")
    )
    for p in candidates:
        stamp = p.stem
        if led["delivered"].get(stamp, {}).get("ok") and not force:
            continue
        r = deliver_stamp(stamp, chat_id, force=force, dry_run=dry_run)
        out.append({"stamp": stamp, **r})
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="哨兵 Telegram 確定性投遞器")
    ap.add_argument("--report", help="報告檔路徑")
    ap.add_argument("--stamp", help="報告時間戳，例如 2026-11-03-21")
    ap.add_argument("--rescue-missing", action="store_true", help="補投遞所有未投遞嘅過閘報告")
    ap.add_argument("--list", action="store_true", help="列出投遞狀態")
    ap.add_argument("--force", action="store_true", help="即使已投遞過都再送一次")
    ap.add_argument("--dry-run", action="store_true", help="唔真送，只試跑")
    ap.add_argument("--chat-id", default=os.environ.get("TELEGRAM_HOME_CHANNEL") or "8475453959")
    args = ap.parse_args()

    if args.list:
        led = load_ledger()
        for stamp in sorted(led["delivered"]):
            r = led["delivered"][stamp]
            print(f"{stamp}  chars={r.get('chars')}  {r.get('delivered_utc')}")
        return 0

    if args.rescue_missing:
        results = rescue_missing(args.chat_id, force=args.force, dry_run=args.dry_run)
        for r in results:
            print(json.dumps(r, ensure_ascii=False))
        ok = sum(1 for r in results if r.get("ok"))
        log(f"rescue 完成：{ok}/{len(results)} 成功")
        return 0 if ok == len(results) else 1

    stamp = args.stamp
    if args.report:
        stamp = Path(args.report).stem
    if not stamp:
        ap.error("要 --report 或 --stamp 或 --rescue-missing")
    res = deliver_stamp(stamp, args.chat_id, force=args.force, dry_run=args.dry_run)
    print(json.dumps(res, ensure_ascii=False))
    return 0 if res.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
