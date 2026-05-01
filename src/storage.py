import json
import os

DB_PATH = "history.json"

def save_to_history(password):
    history = load_history()
    history.append(password)
    if len(history) > 20:
        history.pop(0)
    
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

def load_history():
    if not os.path.exists(DB_PATH):
        return []
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []