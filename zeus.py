
print("================================")
print("        ZEUS v0.3 ONLINE")
print("================================")
print()
print("Greetings, Keith.")
print("The Zeus system is operational.")
print()

MEMORY_FILE = "memory.txt"


def remember(fact):
    try:
        with open(MEMORY_FILE, "r") as file:
            memories = [memory.strip() for memory in file.readlines()]

        if fact in memories:
            print("ZEUS: I already know that.")
            return

    except FileNotFoundError:
        pass

    with open(MEMORY_FILE, "a") as file:
        file.write(fact + "\n")

    print("ZEUS: I will remember that.")


def show_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            memories = file.readlines()

        print("ZEUS MEMORY:")

        for memory in memories:
            print("-", memory.strip())

    except FileNotFoundError:
        print("ZEUS: My memory is empty.")


def status():
    print("ZEUS: All systems operational.")


def hello():
    print("ZEUS: Greetings, Keith.")


def help_menu():
    print("ZEUS COMMANDS:")
    print("- hello")
    print("- status")
    print("- memory")
    print("- remember <something>")
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
            print("ZEUS: Tell me what you want me to remember.")

    elif command.lower() == "help":
        help_menu()

    elif command.lower() in ["quit", "exit"]:
        return False

    else:
        print("ZEUS: I don't understand that command yet.")

    return True


while True:
    command = input("YOU: ")

    if not process_command(command):
        print("ZEUS: Shutting down. Until next time.")
        break