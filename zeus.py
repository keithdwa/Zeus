
print("================================")
print("        ZEUS v0.2 ONLINE")
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


while True:
    command = input("YOU: ").strip()

    if command.lower() == "status":
        print("ZEUS: All systems operational.")

    elif command.lower() == "hello":
        print("ZEUS: Greetings, Keith.")

    elif command.lower().startswith("remember "):
        fact = command[9:]
        remember(fact)

    elif command.lower() == "memory":
        show_memory()

    elif command.lower() in ["quit", "exit"]:
        print("ZEUS: Shutting down. Until next time.")
        break

    else:
        print("ZEUS: I don't understand that command yet.")