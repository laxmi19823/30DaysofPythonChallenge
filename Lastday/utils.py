import json

def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

def evaluate_answer(user_answer, keywords):
    user_answer = user_answer.lower()
    match_count = sum(1 for keyword in keywords if keyword.lower() in user_answer)
    total_keywords = len(keywords)
    return match_count, total_keywords