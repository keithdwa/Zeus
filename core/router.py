from core.memory import Memory
from core.tasks import TaskManager
from core.brain import Brain
from agents import AgentRegistry


class ZeusRouter:
    def __init__(self):
        self.brain = Brain()
        self.memory = Memory()
        self.tasks = TaskManager()
        self.agents = AgentRegistry()

    def handle(self, command):
        command = command.strip()

        if command.lower().startswith("ask "):
            return self.route_agent(command[4:])

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
                    "{}. [{}] {}".format(
                        number,
                        task["status"],
                        task["task"]
                    )
                )

            return "\n".join(lines)

        if intent == "complete_task":
            if self.tasks.complete(decision["data"]):
                return "Task completed."

            return "That task number does not exist."

        if intent == "shutdown":
            return "__SHUTDOWN__"

        return decision["response"]

    def route_agent(self, request):
        parts = request.split(" ", 1)

        if len(parts) < 2:
            return "Specify an agent and a task."

        agent_name = parts[0]
        task = parts[1]

        agent = self.agents.get(agent_name)

        if not agent:
            available = ", ".join(
                agent["name"]
                for agent in self.agents.list_agents()
            )

            return "Unknown agent. Available agents: " + available

        return agent.execute(task)