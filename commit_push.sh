#!/usr/bin/env bash
# 科研哨兵 — 安全 commit + push
# 用法: ./commit_push.sh "commit message"
# 規則:
#   - 不互動（git 絕不要求輸入密碼）
#   - push 失敗最多重試 2 次
#   - 輸出保持簡短（一行狀態 + 錯誤摘要），避免污染 agent context
set -uo pipefail

export GIT_TERMINAL_PROMPT=0
export GIT_ASKPASS=/bin/true
export GIT_SSH_COMMAND="ssh -o BatchMode=yes -o StrictHostKeyChecking=no"

REPO="/root/.hermes/sentinel"
MSG="${1:-chore: sentinel auto commit}"
cd "$REPO" || { echo "PUSH_FAIL: cd $REPO failed"; exit 1; }

if ! git diff --quiet 2>/dev/null || ! git diff --cached --quiet 2>/dev/null; then
  git add -A || { echo "PUSH_FAIL: git add failed"; exit 1; }
  git commit -q -m "$MSG" || { echo "PUSH_FAIL: git commit failed"; exit 1; }
  echo "COMMITTED: $MSG"
else
  # 仍然提交空 commit 以記錄本次運作痕跡（狀態檔 / topics.json 有變動時會自然觸發）
  echo "COMMITTED: nothing to commit (no changes)"
fi

for attempt in 1 2; do
  if git push origin master 2>/tmp/.sentinel_push_err; then
    echo "PUSH_OK: $(git rev-parse --short HEAD) -> origin/master"
    exit 0
  fi
  sleep 3
done

echo "PUSH_FAIL: $(tr '\n' ' ' < /tmp/.sentinel_push_err | head -c 300)"
exit 1
