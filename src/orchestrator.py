from .planner_agent import StudyPlannerAgent
from .evaluator_agent import EvaluatorAgent
from .wellness_agent import WellnessAgent
from .memory import MemoryBank
from .tools import SaveTool

planner = StudyPlannerAgent()
evaluator = EvaluatorAgent()
wellness = WellnessAgent()
memory = MemoryBank()
save_tool = SaveTool()

def run(request):
    goals = request.get("task", "Prepare for exams")
    plan = planner.generate_plan(goals)
    quiz = evaluator.run_quiz()
    mood = wellness.check()

    result = {
        "study_plan": plan,
        "quiz_result": quiz,
        "wellness_status": mood
    }

    save_tool.save(result)
    memory.store("latest_run", result)

    return result
