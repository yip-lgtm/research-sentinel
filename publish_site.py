#!/usr/bin/env python3
"""科研哨兵 — 靜態站發佈器（把 reports/ + knowledge/ 推上 GitHub Pages）

流程：
  1. build_site.py → 生成 gh-pages/R&D/ 靜態站（決定性輸出，冇變動唔會產生 diff）
  2. 寫入 /research/ 別名頁（& 喺 URL 唔好打，用 redirect 引导）
  3. gh-pages repo：git add → commit → pull --rebase → push

點解要 pull --rebase：
  gh-pages repo 同時有 5 個 GitHub Actions workflow 喺寫入（cute/、yipmma/ 等）。
  裸 push 會被拒（non-fast-forward），rebase 會保住自己嘅檔案同時唔會丟失對方改動。

只做機械動作，唔會修改報告正文。
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HERMES_HOME", "/root/.hermes"))
REPO = HERMES_HOME / "sentinel"
PAGES_REPO = Path(os.environ.get("PAGES_REPO", "/root/gh-pages"))
BUILD = REPO / "build_site.py"
OUT = PAGES_REPO / "R&D"
ALIAS_DIR = PAGES_REPO / "research"

ALIAS_HTML = """<!doctype html>
<html lang="zh-HK">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta http-equiv="refresh" content="0; url=/R&amp;D/" />
<title>科研哨兵 · R&amp;D</title>
<link rel="canonical" href="/R&amp;D/" />
<style>html,body{margin:0;background:#000;color:#fff;font-family:-apple-system,BlinkMacSystemFont,"Noto Sans TC","PingFang HK",sans-serif;display:flex;align-items:center;justify-content:center;height:100vh}a{color:#7fb0ff}</style>
</head>
<body>
<p>導向中… <a href="/R&amp;D/">科研哨兵 R&amp;D 研究站</a></p>
<script>location.replace("/R&D/" + location.search + location.hash);</script>
</body>
</html>
"""


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {msg}", flush=True)


def run(cmd, cwd=None, timeout=180):
    try:
        return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    except Exception as exc:  # noqa: BLE001
        return subprocess.CompletedProcess(cmd, 1, "", str(exc))


def git(*args, timeout=180):
    return run(["git", *args], cwd=str(PAGES_REPO), timeout=timeout)


def main() -> int:
    if not PAGES_REPO.is_dir() or not (PAGES_REPO / ".git").exists():
        log(f"publish_site: SKIP — pages repo 唔存在: {PAGES_REPO}")
        return 0
    if not BUILD.exists():
        log("publish_site: SKIP — build_site.py 唔存在")
        return 0

    # 1) build
    r = run([sys.executable, str(BUILD)], cwd=str(REPO), timeout=180)
    build_out = (r.stdout or "").strip().replace("\n", " | ")
    log(f"publish_site: build -> rc={r.returncode} {build_out[:200]}")
    if r.returncode != 0:
        log(f"publish_site: build 失敗: {(r.stderr or '')[:300]}")
        return 1

    # 2) alias（/research/ → /R&D/）
    ALIAS_DIR.mkdir(parents=True, exist_ok=True)
    alias_file = ALIAS_DIR / "index.html"
    if not alias_file.exists() or alias_file.read_text(encoding="utf-8") != ALIAS_HTML:
        alias_file.write_text(ALIAS_HTML, encoding="utf-8")
        log("publish_site: alias /research/ 已更新")

    # 3) git sync
    status = git("status", "--porcelain")
    if status.returncode != 0:
        log(f"publish_site: git status 失敗: {(status.stderr or '')[:200]}")
        return 1
    if not status.stdout.strip():
        log("publish_site: pages repo 冇變動，唔使 push")
        return 0

    git("add", "--all")
    if git("diff", "--cached", "--quiet").returncode == 0:
        log("publish_site: staged 冇變動，跳過")
        return 0

    msg = f"sentinel: publish R&D static site {time.strftime('%Y-%m-%d %H:%M', time.gmtime())} UTC"
    c = git("-c", "user.name=research-sentinel", "-c", "user.email=sentinel@local",
            "commit", "-q", "-m", msg)
    if c.returncode != 0:
        log(f"publish_site: commit 失敗: {(c.stderr or '')[:300]}")
        return 1
    log(f"publish_site: committed -> {msg}")

    # rebase 先 push（gh-pages 有其他 workflow 同時寫入）
    rb = git("pull", "--rebase", "--autostash", "origin", "main", timeout=240)
    if rb.returncode != 0:
        log(f"publish_site: rebase 警告（照試 push）: {(rb.stderr or rb.stdout or '')[:200]}")

    for attempt in (1, 2, 3):
        p = git("push", "origin", "main", timeout=240)
        if p.returncode == 0:
            sha = git("rev-parse", "--short", "HEAD").stdout.strip()
            log(f"publish_site: PUSH_OK {sha} -> origin/main (attempt {attempt})")
            return 0
        log(f"publish_site: push 第 {attempt} 次失敗: {(p.stderr or '')[:200]}")
        time.sleep(5)
        git("pull", "--rebase", "--autostash", "origin", "main", timeout=240)

    log("publish_site: PUSH_FAIL — 連續 3 次 push 失敗")
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001
        log(f"publish_site: FATAL {exc}")
        sys.exit(0)
