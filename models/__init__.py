from models.provider import ModelProvider
from models.local import LocalTestModel
from models.openai_provider import OpenAIProvider


class ModelRegistry:
    def __init__(self):
        self.models = {}

        self.register(LocalTestModel())

        if OpenAIProvider().api_key:
            self.register(OpenAIProvider())

    def register(self, model):
        self.models[model.name.lower()] = model

    def get(self, name):
        return self.models.get(name.lower())

    def default(self):
        if "openai" in self.models:
            return self.models["openai"]

        if not self.models:
            return None

        return next(iter(self.models.values()))

    def list_models(self):
        return [
            model.name
            for model in self.models.values()
        ]