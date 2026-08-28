from agents.base import Agent
from models import ModelRegistry


class Athena(Agent):
    name = "Athena"
    role = "Strategy, planning and analysis"

    def __init__(self):
        super().__init__()
        self.models = ModelRegistry()

    def think(self, task):
        task = task.strip()

        if not task:
            return "Athena needs a task to analyse."

        prompt = (
            "You are Athena, the strategy and analysis agent "
            "within the Zeus AI ecosystem.\n\n"
            "Analyse the following task:\n\n"
            "{}\n\n"
            "Provide objectives, constraints, risks and recommended actions."
        ).format(task)

        model = self.models.default()

        if not model:
            return "Athena has no model available."

        return model.generate(prompt)

    def execute(self, task):
        return self.think(task)