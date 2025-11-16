from google.generativeai import GenerativeModel
import os
from google.generativeai import configure

configure(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_KEY"))
model = GenerativeModel("gemini-1.5-flash")

class StudyPlannerAgent:
    def generate_plan(self, goals):
        prompt = f"Create a weekly study plan for: {goals}"
        response = model.generate_content(prompt)
        return response.text
