import json

with open("students.json", "r", encoding="utf-8") as f:
    talabalar = json.load(f)

eng_yaxshi = max(talabalar, key=lambda t: t["grade"])

eng_past = min(talabalar, key=lambda t: t["grade"])

umumiy_baho = sum(t["grade"] for t in talabalar)

o_rtacha = round(umumiy_baho / len(talabalar), 1)

print(f"Eng yaxshi talaba: {eng_yaxshi['name']} — {eng_yaxshi['grade']}")
print(f"Eng past baho: {eng_past['name']} — {eng_past['grade']}")
print(f"O'rtacha baho: {o_rtacha}")