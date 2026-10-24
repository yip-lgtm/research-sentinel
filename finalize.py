#!/usr/bin/env python3
"""人性化練習哨兵 — 確定性 finalizer（不依賴 LLM）

存在的理由：每小時 cron 個 LLM 步驟有工具呼叫上限。撞上限時佢會停喺
「研究完成、但未存檔、未過品質閘、未 commit」嘅狀態，於是：
  - 交付層：cron 個 Response 仍然送到用戶（內容本身可能合規）
  - 持久化層：reports/ 無檔、state.json 無更新、git 無 commit
  - keepalive：因為無 commit，所以「冇嘢可推」→ 自動 push 從來冇生效

finalizer 負責補返呢一層，規則全部係確定性嘅，唔問 LLM：
  1. 讀最新一次 cron 輸出（Response 段）
  2. 若 reports/{YYYY-MM-DD-HH}.md 唔存在 → 由 Response 抽檔存檔（記錄實際交付咗乜）
  3. 跑 quality_gate.py，把結果記錄落 reports/index.json（唔污染報告正文）
  4. commit + push（git add -A，任何改動都會推，包括 untracked 新檔）

只做機械動作，絕不修改報告正文內容。
"""
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HERMES_HOME", "/root/.hermes"))
REPO = HERMES_HOME / "sentinel"
CRON_OUT = HERMES_HOME / "cron" / "output"
JOB_ID = "a1d898e84805"
REPORTS = REPO / "reports"
INDEX = REPORTS / "index.json"
GATE = REPO / "quality_gate.py"
PUBLISH = REPO / "publish_site.py"
ARCHIVE = REPORTS / "archive"


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {msg}", flush=True)


def run(cmd, cwd=None, timeout=120):
    try:
        return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    except Exception as exc:  # noqa: BLE001
        return subprocess.CompletedProcess(cmd, 1, "", str(exc))


def load_index() -> dict:
    if INDEX.exists():
        try:
            return json.loads(INDEX.read_text())
        except Exception:
            pass
    return {"reports": {}, "updated_utc": None}


def save_index(idx: dict) -> None:
    idx["updated_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    tmp = INDEX.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(idx, ensure_ascii=False, indent=2))
    os.replace(tmp, INDEX)


def latest_cron_output():
    d = CRON_OUT / JOB_ID
    if not d.is_dir():
        return None
    files = sorted(d.glob("*.md"))
    return files[-1] if files else None


def extract_response(text: str) -> str:
    """抽出 cron 輸出嘅 Response 段（去 markdown 標題層級無關）。"""
    m = re.search(r"^##\s+Response\s*$", text, re.M)
    body = text[m.end():] if m else text
    return body.strip()


def looks_like_report(body: str) -> bool:
    need = ["主題", "核心發現", "潛在影響", "來源依據", "簡評"]
    return all(k in body for k in need)


def run_gate(path: Path) -> dict:
    r = run([sys.executable, str(GATE), str(path), "--json"])
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"pass": False, "fails": [f"gate 執行失敗: {r.stderr[:200]}"], "warnings": []}


def archive_failed(stamp: str, target: Path, entry: dict) -> dict:
    """未過品質閘嘅草稿 → mv 去 reports/archive/ + index 標 archived:true。

    SOUL.md 硬規則：未過閘草稿唔上架。build_site.py 已會跳過 gate_pass=False，
    但呢度補埋「檔案本身移走 + index 標記」，令 archive 成為單一事實來源。
    """
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    dest = ARCHIVE / target.name
    if target.parent.resolve() == ARCHIVE.resolve():
        # 已經喺 archive 里面，唔使再搬
        entry["archived"] = True
        entry.setdefault("archived_utc", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
        entry.setdefault("archived_from", str(target))
        return entry
    if dest.exists():
        dest.unlink()
    try:
        target.rename(dest)
    except OSError as exc:
        log(f"finalize: archive 搬移失敗 {target.name} — {exc}")
        return entry
    entry["archived"] = True
    entry["archived_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    entry["archived_from"] = str(target)
    log(f"finalize: 未過品質閘 {stamp} → archive/{target.name}")
    return entry


def git_has_changes() -> bool:
    r = run(["git", "status", "--porcelain"], cwd=str(REPO))
    return r.returncode == 0 and bool(r.stdout.strip())


def git_ahead() -> int:
    r = run(["git", "rev-list", "--count", "@{u}..HEAD"], cwd=str(REPO))
    if r.returncode != 0:
        return 0
    try:
        return int(r.stdout.strip() or "0")
    except ValueError:
        return 0


def sync_git(message: str) -> str:
    """任何工作區改動或未推送 commit → commit_push.sh（已修 untracked bug）。"""
    if not git_has_changes() and git_ahead() == 0:
        return "nothing-to-push"
    script = REPO / "commit_push.sh"
    r = run(["bash", str(script), message], cwd=str(REPO), timeout=180)
    out = (r.stdout or "").strip().replace("\n", " | ")
    return out[:300] or f"push_rc={r.returncode}"


def main() -> None:
    idx = load_index()

    src = latest_cron_output()
    if src is None:
        log("finalize: 搵唔到 cron 輸出，跳過存檔，只做 git 同步")
    else:
        raw = src.read_text(errors="ignore")
        body = extract_response(raw)
        # 從檔名取時間戳：2026-10-22_15-32-20.md
        m = re.match(r"(\d{4}-\d{2}-\d{2})_(\d{2})-", src.name)
        stamp = f"{m.group(1)}-{m.group(2)}" if m else src.stem

        if stamp not in idx["reports"] and looks_like_report(body):
            REPORTS.mkdir(parents=True, exist_ok=True)
            target = REPORTS / f"{stamp}.md"
            if not target.exists():
                target.write_text(body + "\n", encoding="utf-8")
                log(f"finalize: 已由 cron Response 存檔 -> {target.name} ({target.stat().st_size} bytes)")
            gate = run_gate(target)
            entry = {
                "source": str(src),
                "bytes": gate.get("bytes", target.stat().st_size),
                "cjk": gate.get("cjk"),
                "sources": gate.get("sources"),
                "gate_pass": bool(gate.get("pass")),
                "fails": gate.get("fails", []),
                "warnings": gate.get("warnings", []),
                "archived_by": "finalize.py",
            }
            if not gate.get("pass"):
                entry = archive_failed(stamp, target, entry)
            idx["reports"][stamp] = entry
            save_index(idx)
            log(f"finalize: 品質閘 {stamp} -> {'PASS' if gate.get('pass') else 'FAIL'}"
                + ("" if gate.get("pass") else f" {gate.get('fails')}"))
        elif stamp not in idx["reports"]:
            log(f"finalize: {stamp} Response 不似完整報告（五段缺漏），只做 git 同步")
        else:
            # 已存檔但可能被人手修正（例如修 H6 項目符號、切 bytes）→ 重跑品質閘更新 index
            target = REPORTS / f"{stamp}.md"
            archived_path = ARCHIVE / f"{stamp}.md"
            # 之前未過閘被 archive 咗，但可能已經人手修好 → 試下拉返上嚟
            if not target.exists() and archived_path.exists():
                cand = run_gate(archived_path)
                if cand.get("pass"):
                    target.parent.mkdir(parents=True, exist_ok=True)
                    archived_path.rename(target)
                    log(f"finalize: {stamp} 已修正過閘，從 archive 拉回 reports/")
                else:
                    target = archived_path
            if target.exists():
                gate = run_gate(target)
                old = idx["reports"].get(stamp, {})
                new_entry = {
                    "source": old.get("source", str(src)),
                    "bytes": gate.get("bytes", target.stat().st_size),
                    "cjk": gate.get("cjk"),
                    "sources": gate.get("sources"),
                    "gate_pass": bool(gate.get("pass")),
                    "fails": gate.get("fails", []),
                    "warnings": gate.get("warnings", []),
                    "archived_by": "finalize.py",
                    "reverified_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                }
                if old.get("archived"):
                    new_entry["archived"] = True
                # 未過閘 → 移去 archive（人手修正咗就唔好搬走）
                if not gate.get("pass") and not old.get("archived"):
                    new_entry = archive_failed(stamp, target, new_entry)
                # 索引任何時候都要反映當前檔案實況（bytes/cjk 會因人手修正而變）
                if old.get("gate_pass") != new_entry["gate_pass"] or \
                   old.get("fails") != new_entry["fails"] or \
                   old.get("bytes") != new_entry["bytes"] or \
                   old.get("cjk") != new_entry["cjk"] or \
                   old.get("archived") != new_entry.get("archived"):
                    reason = []
                    if old.get("gate_pass") != new_entry["gate_pass"] or old.get("fails") != new_entry["fails"]:
                        reason.append(f"品質閘 -> {'PASS' if gate.get('pass') else 'FAIL'}"
                                      + ("" if gate.get("pass") else f" {gate.get('fails')}"))
                    if old.get("bytes") != new_entry["bytes"]:
                        reason.append(f"bytes {old.get('bytes')} -> {new_entry['bytes']}")
                    idx["reports"][stamp] = new_entry
                    save_index(idx)
                    log(f"finalize: 重驗 {stamp} — {'；'.join(reason)}")

    msg = f"chore: sentinel sync {time.strftime('%Y-%m-%d %H:%M', time.gmtime())} UTC"
    res = sync_git(msg)
    log(f"finalize: git -> {res}")

    # 靜態站發佈：有新報告就 build + push 上 GitHub Pages
    if PUBLISH.exists():
        pr = run([sys.executable, str(PUBLISH)], cwd=str(REPO), timeout=300)
        out = (pr.stdout or "").strip().replace("\n", " | ")
        log(f"finalize: publish_site -> rc={pr.returncode} {out[:300]}")
        if pr.returncode != 0:
            log(f"finalize: publish_site 錯誤 {(pr.stderr or '')[:200]}")
    else:
        log("finalize: publish_site.py 唔存在，靜態站未更新")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        log(f"FATAL: {exc}")
    sys.exit(0)
