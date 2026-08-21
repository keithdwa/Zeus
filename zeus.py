print("================================")
print("        ZEUS v0.1 ONLINE")
print("================================")
print()
print("Greetings, Keith.")
print("The Zeus system is operational.")
print()

while True:
    command = input("YOU: ")

    if command.lower() == "status":
        print("ZEUS: All systems operational.")
    elif command.lower() == "hello":
        print("ZEUS: Greetings, Keith.")
    elif command.lower() in ["quit", "exit"]:
        print("ZEUS: Shutting down. Until next time.")
        break
    else:
        print("ZEUS: I don't understand that command yet.")