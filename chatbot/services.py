import json,random,re
from pathlib import Path
DATA=Path(__file__).resolve().parent.parent/"data"/"knowledge.json"

def norm(s):
    return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9 ]"," ",s.lower())).strip()

def answer_question(message):
    user=norm(message); words=set(user.split())
    with open(DATA,encoding="utf-8") as f: items=json.load(f)["questions"]
    best=None; best_score=0
    for item in items:
        q=norm(item["question"]); keys=[norm(k) for k in item.get("keywords",[])]
        score=10 if user==q else 0
        score += sum(2 for w in words if w in q.split())
        score += sum(3 for w in words for k in keys if w==k or w in k.split())
        score += sum(5 for k in keys if k and k in user)
        if score>best_score: best_score,best=score,item
    if not best or best_score<3:
        return {"answer":"I don't have an answer for that yet. Try a suggested question.","follow_up":["What is Django?","What is Python?","What can you do?"]}
    return {"answer":random.choice(best["answers"]),"follow_up":best.get("follow_up",[])}
