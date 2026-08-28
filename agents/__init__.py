from agents.athena import Athena


class AgentRegistry:
    def __init__(self):
        self.agents = {}

        self.register(Athena())

    def register(self, agent):
        self.agents[agent.name.lower()] = agent

    def get(self, name):
        return self.agents.get(name.lower())

    def list_agents(self):
        return [
            agent.describe()
            for agent in self.agents.values()
        ]