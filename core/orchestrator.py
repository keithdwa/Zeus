class Orchestrator:
    def __init__(self, registry):
        self.registry = registry

    def available_agents(self):
        return self.registry.list_agents()

    def choose_agents(self, task):
        task_lower = task.lower()
        selected = []

        if any(word in task_lower for word in [
            "plan", "strategy", "analyse", "analysis",
            "decision", "architecture", "problem"
        ]):
            selected.append("athena")

        if not selected:
            selected.append("athena")

        return selected

    def run(self, task):
        agent_names = self.choose_agents(task)
        results = []

        for name in agent_names:
            agent = self.registry.get(name)

            if agent:
                results.append({
                    "agent": agent.name,
                    "result": agent.execute(task)
                })

        return results