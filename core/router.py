from core.memory import Memory
from core.tasks import TaskManager
from core.brain import Brain


class ZeusRouter:
    def __init__(self):
        self.brain = Brain()
        self.memory = Memory()
        self.tasks = TaskManager()

    def handle(self, command):
        decision = self.brain.think(command)
        intent = decision["intent"]

        if intent == "greeting":
            return decision["response"]

        if intent == "status":
            return decision["response"]

        if intent == "remember":
            self.memory.remember(decision["data"])
            return "Memory updated."

        if intent == "add_task":
            self.tasks.add(decision["data"])
            return "Task added."

        if intent == "list_tasks":
            tasks = self.tasks.list()

            if not tasks:
                return "There are no tasks."

            lines = []

            for number, task in enumerate(tasks, 1):
                lines.append(
                    f"{number}. [{task['status']}] {task['task']}"
                )

            return "\n".join(lines)

        if intent == "complete_task":
            if self.tasks.complete(decision["data"]):
                return "Task completed."

            return "That task number does not exist."

        if intent == "shutdown":
            return "__SHUTDOWN__"

        return decision["response"]