class ModelProvider:
    name = "Base Model"

    def generate(self, prompt):
        raise NotImplementedError(
            "Model provider must implement generate()."
        )