CONFIG_FILE = "config.txt"
MEMORY_FILE = "memory.txt"


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
VERSION = config.get("VERSION", "0.5")
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