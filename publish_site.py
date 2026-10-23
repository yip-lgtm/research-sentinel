#!/usr/bin/env python3
"""人性化練習哨兵 — 靜態站發佈器（把 reports/ + knowledge/ 推上 GitHub Pages）

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


def run(cmd, cwd=None, timeout=180, env=None):
    try:
        return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                              timeout=timeout, env=env)
    except Exception as exc:  # noqa: BLE001
        return subprocess.CompletedProcess(cmd, 1, "", str(exc))


GIT_ENV = {
    # 1) 冇 user.name/user.email → `git rebase` 喺 pick 階段 fatal，
    #    留低 "interactive rebase in progress" 爛狀態，之後所有 push 被拒。
    "GIT_AUTHOR_NAME": "research-sentinel",
    "GIT_AUTHOR_EMAIL": "sentinel@local",
    "GIT_COMMITTER_NAME": "research-sentinel",
    "GIT_COMMITTER_EMAIL": "sentinel@local",
    # 2) 非互動環境冇 editor → rebase 停喺要你改 commit message 嗰步。
    "GIT_EDITOR": "true",
    "GIT_SEQUENCE_EDITOR": "true",
}


def git(*args, timeout=180):
    env = dict(os.environ)
    env.update(GIT_ENV)
    return run(["git", *args], cwd=str(PAGES_REPO), timeout=timeout, env=env)


def ensure_repo_usable() -> str:
    """修爛嘅 git 狀態。

    歷史教訓：20:09 嗰次 `git pull --rebase` 因為缺 user.email + 缺 editor
    卡死喺 "interactive rebase in progress"，之後每次 publish 都 commit 落
    detached HEAD，push 全部被 non-fast-forward 拒絕 → 線上站停咗 4 個鐘。

    呢度做防護：偵測到 rebase 中途就 abort 佢，並把 HEAD 拉返去 main。
    """
    gitdir = PAGES_REPO / ".git"
    for d in ("rebase-merge", "rebase-apply"):
        if (gitdir / d).is_dir():
            log(f"publish_site: 偵測到爛 rebase 狀態 ({d})，自動 abort")
            git("rebase", "--abort")
            # abort 之後可能仍然 detached HEAD → 拉返 main
            head = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
            if head != "main":
                log(f"publish_site: HEAD 係 '{head}'，checkout main")
                git("checkout", "main")
                git("reset", "--hard", "origin/main")
    # 分支追唔上 remote → 直接同步（用 merge backend，避免 interactive rebase）
    br = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if br != "main":
        git("checkout", "main")
    git("-c", "rebase.backend=merge", "fetch", "origin", "main", timeout=240)
    return "repo-ok"


def main() -> int:
    if not PAGES_REPO.is_dir() or not (PAGES_REPO / ".git").exists():
        log(f"publish_site: SKIP — pages repo 唔存在: {PAGES_REPO}")
        return 0
    if not BUILD.exists():
        log("publish_site: SKIP — build_site.py 唔存在")
        return 0

    # 0) 先確保 git 狀態健康（rebase 殘留 / detached HEAD）
    try:
        ensure_repo_usable()
    except Exception as exc:  # noqa: BLE001
        log(f"publish_site: ensure_repo_usable 警告: {exc}")

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
    # 用 merge backend + 明確 autostash，避免落 interactive rebase（需要 editor）。
    rb = git("-c", "rebase.backend=merge", "-c", "rebase.autoStash=true",
             "pull", "--rebase", "origin", "main", timeout=240)
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
        git("-c", "rebase.backend=merge", "-c", "rebase.autoStash=true",
            "pull", "--rebase", "origin", "main", timeout=240)

    log("publish_site: PUSH_FAIL — 連續 3 次 push 失敗")
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001
        log(f"publish_site: FATAL {exc}")
        sys.exit(0)
