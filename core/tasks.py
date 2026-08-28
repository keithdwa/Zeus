import os


class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename

    def add(self, task):
        with open(self.filename, "a") as file:
            file.write("PENDING|" + task.strip() + "\n")

    def list(self):
        if not os.path.exists(self.filename):
            return []

        tasks = []

        with open(self.filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split("|", 1)

                if len(parts) == 2:
                    tasks.append({
                        "status": parts[0],
                        "task": parts[1]
                    })

        return tasks

    def complete(self, task_number):
        tasks = self.list()

        if task_number < 1 or task_number > len(tasks):
            return False

        tasks[task_number - 1]["status"] = "DONE"

        with open(self.filename, "w") as file:
            for task in tasks:
                file.write(
                    task["status"] + "|" + task["task"] + "\n"
                )

        return True