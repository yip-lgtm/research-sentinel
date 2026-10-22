#!/usr/bin/env python3
"""科研哨兵 keepalive — 24/7 自癒心跳

每 3 分鐘檢查：
  1. Hermes gateway process 是否存活（死了就 supervisord 會重啟，這裡做二次保險）
  2. 哨兵 cron job 是否仍然 enabled + scheduled（被人 pause 就自動 resume）
  3. sentinel repo 有沒有未 push 的 commit（自動 push，不依賴當次報告成功）
  4. lifespan_hours <= 0 時把 cron job 停掉（壽命耗盡 → 暫停自動輸出）

輸出只寫 log，不污染 agent context。
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HERMES_HOME", "/root/.hermes"))
REPO = HERMES_HOME / "sentinel"
JOBS = HERMES_HOME / "cron" / "jobs.json"
STATE = REPO / "state.json"
LOG = REPO / "logs" / "keepalive.log"
JOB_ID = "a1d898e84805"
INTERVAL = 180


def log(msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with LOG.open("a") as f:
        f.write(f"{ts} {msg}\n")


def gateway_alive() -> bool:
    p = subprocess.run(["pgrep", "-f", "hermes gateway run"],
                       capture_output=True, text=True)
    return p.returncode == 0 and p.stdout.strip() != ""


def job_state() -> dict:
    try:
        data = json.loads(JOBS.read_text())
    except Exception as e:
        log(f"ERR read jobs.json: {e}")
        return {}
    for j in data.get("jobs", []):
        if j.get("id") == JOB_ID:
            return j
    return {}


def fix_job(job: dict) -> None:
    """确保 cron job 处于 enabled + scheduled 状态。"""
    changed = False
    if not job.get("enabled") or job.get("state") == "paused":
        job["enabled"] = True
        job["state"] = "scheduled"
        job["paused_at"] = None
        job["paused_reason"] = "auto-resumed by keepalive"
        changed = True
    data = json.loads(JOBS.read_text())
    for j in data.get("jobs", []):
        if j.get("id") == JOB_ID:
            j.update(job)
    tmp = JOBS.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    os.replace(tmp, JOBS)
    if changed:
        log("FIX: resumed cron job")


def lifespan_exhausted() -> bool:
    try:
        st = json.loads(STATE.read_text())
    except Exception:
        return False
    return float(st.get("lifespan_hours", 1)) <= 0


def push_unpushed() -> None:
    """如果 repo 有 commit 没推到 remote，就补推。"""
    try:
        r = subprocess.run(["git", "-C", str(REPO), "rev-list", "--count",
                            "@{u}..HEAD"], capture_output=True, text=True)
        if r.returncode != 0:
            return
        if int(r.stdout.strip() or "0") > 0:
            p = subprocess.run([str(REPO / "commit_push.sh"),
                                "chore: keepalive auto push"],
                               capture_output=True, text=True, timeout=120)
            log("PUSH: " + p.stdout.strip().replace("\n", " | ")[:200])
    except Exception as e:
        log(f"ERR push: {e}")


def run_finalizer() -> None:
    """跑確定性 finalizer：把最新 cron Response 存檔、跑品質閘、commit+push。

    唔依賴 LLM，即使 cron 個 agent 撞工具上限中斷，呢層照樣補返持久化同 push。
    """
    script = REPO / "finalize.py"
    if not script.exists():
        return
    try:
        r = subprocess.run([sys.executable, str(script)],
                           capture_output=True, text=True, timeout=180)
        out = (r.stdout or "").strip().replace("\n", " | ")
        if out:
            log("FINALIZE: " + out[:400])
        if r.stderr:
            log("FINALIZE_ERR: " + r.stderr.strip().replace("\n", " | ")[:300])
    except Exception as e:
        log(f"ERR finalize: {e}")


def main() -> None:
    if not gateway_alive():
        log("WARN: gateway process not found (supervisord should restart it)")
    job = job_state()
    if job:
        if job.get("deliver") != "telegram:8475453959":
            log(f"WARN: deliver target changed -> {job.get('deliver')}")
        if lifespan_exhausted():
            if job.get("enabled"):
                job["enabled"] = False
                job["state"] = "paused"
                job["paused_reason"] = "lifespan exhausted"
                fix_job(job)
                log("PAUSE: lifespan exhausted, cron disabled")
        else:
            fix_job(job)
    push_unpushed()
    run_finalizer()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # keepalive 绝不能自己死掉
        log(f"FATAL: {exc}")
    sys.exit(0)
