class Brain:
    def think(self, command):
        command = command.strip()

        if not command:
            return {
                "intent": "empty",
                "response": "I am listening."
            }

        lowered = command.lower()

        if lowered in ["hello", "hi", "hey"]:
            return {
                "intent": "greeting",
                "response": "Greetings, Keith."
            }

        if "status" in lowered:
            return {
                "intent": "status",
                "response": "All core systems are operational."
            }

        if lowered.startswith("remember "):
            return {
                "intent": "remember",
                "data": command[9:].strip()
            }

        if lowered.startswith("add task "):
            return {
                "intent": "add_task",
                "data": command[9:].strip()
            }

        if lowered in ["tasks", "list tasks", "show tasks"]:
            return {
                "intent": "list_tasks"
            }

        if lowered.startswith("complete task "):
            number = command[14:].strip()

            if number.isdigit():
                return {
                    "intent": "complete_task",
                    "data": int(number)
                }

        if lowered in ["quit", "exit", "shutdown"]:
            return {
                "intent": "shutdown",
                "response": "Zeus shutting down."
            }

        return {
            "intent": "unknown",
            "response": "I don't have a capability for that yet."
        }