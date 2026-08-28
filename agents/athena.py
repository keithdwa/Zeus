from agents.base import Agent


class Athena(Agent):
    name = "Athena"
    role = "Strategy, planning and analysis"

    def think(self, task):
        task = task.strip()

        if not task:
            return "Athena needs a task to analyse."

        return (
            "ATHENA ANALYSIS\n"
            "Task: {}\n"
            "Approach: Break the problem into objectives, "
            "constraints, risks and actions."
        ).format(task)

    def execute(self, task):
        return self.think(task)