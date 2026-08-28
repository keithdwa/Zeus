from models.provider import ModelProvider


class LocalTestModel(ModelProvider):
    name = "Zeus Local Test Model"

    def generate(self, prompt):
        prompt = prompt.strip()

        if not prompt:
            return "No prompt received."

        return (
            "ZEUS MODEL RESPONSE\n"
            "Prompt received: {}\n"
            "Model interface is operational."
        ).format(prompt)