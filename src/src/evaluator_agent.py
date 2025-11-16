import random

class EvaluatorAgent:
    def run_quiz(self):
        score = random.randint(60, 100)
        return {"score": score, "status": "pass" if score > 70 else "review"}
