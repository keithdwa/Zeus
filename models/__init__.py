from models.provider import ModelProvider
from models.local import LocalTestModel


class ModelRegistry:
    def __init__(self):
        self.models = {}

        self.register(LocalTestModel())

    def register(self, model):
        self.models[model.name.lower()] = model

    def get(self, name):
        return self.models.get(name.lower())

    def default(self):
        if not self.models:
            return None

        return next(iter(self.models.values()))

    def list_models(self):
        return [
            model.name
            for model in self.models.values()
        ]