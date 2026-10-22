#!/usr/bin/env python3
"""科研哨兵 評分 / 壽命管理

用法:
  python3 score.py pass   [主題]   # 合格: +1 級, +5 小時
  python3 score.py full   [主題]   # 滿分: +2 級, +10 小時
  python3 score.py fail   [主題]   # 不合格: -5 小時
  python3 score.py status          # 顯示狀態
  python3 score.py topic <名>      # 顯示某主題表現
"""
import json, sys, os, datetime

STATE = "/root/.hermes/sentinel/state.json"
TOPICS = "/root/.hermes/sentinel/knowledge/topics.json"
MAX_LEVEL = 20
MAX_HOURS = 240

def load(p):
    with open(p) as f: return json.load(f)

def save(p, d):
    tmp = p + ".tmp"
    with open(tmp, "w") as f: json.dump(d, f, ensure_ascii=False, indent=2)
    os.replace(tmp, p)

def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    st = load(STATE)
    sc = st["scoring"]

    if cmd == "status":
        print(f"等級 L{st['level']}  壽命 {st['lifespan_hours']}h / {st['lifespan_hours_max']}h")
        print(f"階段 {st['phase']}  報告 {st['reports_total']} (合格 {st['reports_qualified']} / 滿分 {st['reports_full_score']} / 不合格 {st['reports_rejected']})")
        print(f"最後報告 {st['last_report_utc']}")
        if st.get("foundation_deadline_utc"):
            print(f"基礎建設截止 {st['foundation_deadline_utc']}")
        print("主題表現:", json.dumps(st.get("topic_performance", {}), ensure_ascii=False))
        return

    if cmd == "topic":
        name = sys.argv[2] if len(sys.argv) > 2 else ""
        print(json.dumps(st.get("topic_performance", {}).get(name, {}), ensure_ascii=False, indent=2))
        return

    topic = sys.argv[2] if len(sys.argv) > 2 else "general"
    delta_lv = delta_h = 0
    if cmd == "pass":
        delta_lv, delta_h = sc["pass_gain_level"], sc["pass_gain_hours"]
        st["reports_qualified"] += 1
        st["reports_total"] += 1
    elif cmd == "full":
        delta_lv, delta_h = sc["full_gain_level"], sc["full_gain_hours"]
        st["reports_qualified"] += 1
        st["reports_full_score"] += 1
        st["reports_total"] += 1
    elif cmd == "fail":
        delta_lv, delta_h = 0, -sc["fail_penalty_hours"]
        st["reports_rejected"] += 1
        st["reports_total"] += 1
    else:
        print("unknown cmd"); sys.exit(1)

    st["level"] = min(MAX_LEVEL, st["level"] + delta_lv)
    st["lifespan_hours"] = max(0, st["lifespan_hours"] + delta_h)
    st["lifespan_hours_max"] = max(st["lifespan_hours_max"], st["lifespan_hours"])
    st["last_report_utc"] = now()

    tp = st.setdefault("topic_performance", {})
    t = tp.setdefault(topic, {"pass": 0, "full": 0, "fail": 0, "level": 1})
    t[cmd if cmd != "full" else "full"] = t.get(cmd if cmd != "full" else "full", 0) + 1
    t["level"] = min(MAX_LEVEL, t.get("level", 1) + delta_lv)

    st["history"].append({"utc": now(), "cmd": cmd, "topic": topic,
                          "level": st["level"], "hours": st["lifespan_hours"]})
    st["history"] = st["history"][-200:]

    save(STATE, st)

    if st["lifespan_hours"] <= 0:
        print(f"壽命耗盡 → 已暫停自動輸出 (L{st['level']})")
    else:
        print(f"{cmd}: {topic} → L{st['level']} (+{delta_lv}), 壽命 {st['lifespan_hours']}h (+{delta_h})")

if __name__ == "__main__":
    main()
