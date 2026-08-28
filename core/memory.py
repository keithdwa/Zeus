import os


class Memory:
    def __init__(self, filename="memory.txt"):
        self.filename = filename

    def remember(self, text):
        with open(self.filename, "a") as file:
            file.write(text.strip() + "\n")

    def recall(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:
            return [line.strip() for line in file if line.strip()]

    def search(self, keyword):
        keyword = keyword.lower()
        return [
            item for item in self.recall()
            if keyword in item.lower()
        ]