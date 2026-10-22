#!/usr/bin/env bash
# 科研哨兵 keepalive 循環 — 由 supervisord 托管，確保 24/7 心跳
# 每 180 秒執行一次 keepalive.py
while true; do
  python3 /root/.hermes/sentinel/keepalive.py >> /root/.hermes/sentinel/logs/keepalive.stdout.log 2>&1
  sleep 180
done
