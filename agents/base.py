class Agent:
    name = "Agent"
    role = "General purpose agent"

    def __init__(self):
        self.active = True

    def describe(self):
        return {
            "name": self.name,
            "role": self.role,
            "active": self.active
        }

    def think(self, task):
        return "{} received task: {}".format(self.name, task)

    def execute(self, task):
        return self.think(task)