CONFIG_FILE = "config.txt"
MEMORY_FILE = "memory.txt"
TASK_FILE = "tasks.txt"


def load_config():
    config = {}

    try:
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                line = line.strip()

                if "=" in line:
                    key, value = line.split("=", 1)
                    config[key] = value

    except FileNotFoundError:
        print("ZEUS: Configuration file not found.")

    return config


config = load_config()

NAME = config.get("NAME", "ZEUS")
OWNER = config.get("OWNER", "KEITH")
VERSION = config.get("VERSION", "0.7")
PERSONALITY = config.get("PERSONALITY", "LOYAL, DIRECT, HELPFUL")


print("================================")
print("        " + NAME + " v" + VERSION + " ONLINE")
print("================================")
print()
print("Greetings, " + OWNER + ".")
print("The " + NAME + " system is operational.")
print("Personality: " + PERSONALITY)
print()


def remember(fact):
    try:
        with open(MEMORY_FILE, "r") as file:
            memories = [memory.strip() for memory in file.readlines()]

        if fact in memories:
            print(NAME + ": I already know that.")
            return

    except FileNotFoundError:
        pass

    with open(MEMORY_FILE, "a") as file:
        file.write(fact + "\n")

    print(NAME + ": I will remember that.")


def show_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            memories = file.readlines()

        print(NAME + " MEMORY:")

        for memory in memories:
            print("-", memory.strip())

    except FileNotFoundError:
        print(NAME + ": My memory is empty.")


def forget(fact):
    try:
        with open(MEMORY_FILE, "r") as file:
            memories = [memory.strip() for memory in file.readlines()]

        if fact not in memories:
            print(NAME + ": I don't have that memory.")
            return

        memories = [memory for memory in memories if memory != fact]

        with open(MEMORY_FILE, "w") as file:
            for memory in memories:
                file.write(memory + "\n")

        print(NAME + ": Memory forgotten.")

    except FileNotFoundError:
        print(NAME + ": My memory is empty.")


def add_task(task):
    with open(TASK_FILE, "a") as file:
        file.write("PENDING|" + task + "\n")

    print(NAME + ": Task created.")


def show_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()

        print(NAME + " TASKS:")

        for number, task in enumerate(tasks, 1):
            task = task.strip()

            if "|" in task:
                task_status, description = task.split("|", 1)
            else:
                task_status = "PENDING"
                description = task

            print("-", str(number) + ".", description, "[" + task_status + "]")

    except FileNotFoundError:
        print(NAME + ": I have no tasks.")


def complete_task(task_number):
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [task.strip() for task in file.readlines()]

        if task_number < 1 or task_number > len(tasks):
            print(NAME + ": That task number does not exist.")
            return

        updated_tasks = []

        for number, task in enumerate(tasks, 1):

            if "|" in task:
                task_status, description = task.split("|", 1)
            else:
                task_status = "PENDING"
                description = task

            if number == task_number:
                task_status = "DONE"

            updated_tasks.append(task_status + "|" + description)

        with open(TASK_FILE, "w") as file:
            for task in updated_tasks:
                file.write(task + "\n")

        print(NAME + ": Task completed.")

    except FileNotFoundError:
        print(NAME + ": I have no tasks.")


def status():
    print(NAME + ": All systems operational.")


def hello():
    print(NAME + ": Greetings, " + OWNER + ".")


def help_menu():
    print(NAME + " COMMANDS:")
    print("- hello")
    print("- status")
    print("- memory")
    print("- remember <something>")
    print("- forget <something>")
    print("- task add <something>")
    print("- tasks")
    print("- task done <number>")
    print("- help")
    print("- quit")


def process_command(command):
    command = command.strip()

    if command.lower() == "status":
        status()

    elif command.lower() == "hello":
        hello()

    elif command.lower() == "memory":
        show_memory()

    elif command.lower().startswith("remember "):
        fact = command[9:].strip()

        if fact:
            remember(fact)
        else:
            print(NAME + ": Tell me what you want me to remember.")

    elif command.lower().startswith("forget "):
        fact = command[7:].strip()

        if fact:
            forget(fact)
        else:
            print(NAME + ": Tell me what you want me to forget.")

    elif command.lower().startswith("task add "):
        task = command[9:].strip()

        if task:
            add_task(task)
        else:
            print(NAME + ": Tell me what task you want me to add.")

    elif command.lower() == "tasks":
        show_tasks()

    elif command.lower().startswith("task done "):
        number_text = command[10:].strip()

        if number_text.isdigit():
            complete_task(int(number_text))
        else:
            print(NAME + ": Tell me the task number to complete.")

    elif command.lower() == "help":
        help_menu()

    elif command.lower() in ["quit", "exit"]:
        return False

    else:
        print(NAME + ": I don't understand that command yet.")

    return True


while True:
    command = input("YOU: ")

    if not process_command(command):
        print(NAME + ": Shutting down. Until next time.")
        break