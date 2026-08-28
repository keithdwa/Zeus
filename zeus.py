from core.router import ZeusRouter


def main():
    zeus = ZeusRouter()

    print("================================")
    print("          ZEUS 10")
    print("================================")
    print("Core systems online.")
    print("Memory online.")
    print("Task system online.")
    print("Brain online.")
    print("Router online.")
    print()
    print("Zeus is ready, Keith.")
    print()

    while True:
        command = input("YOU: ")

        response = zeus.handle(command)

        if response == "__SHUTDOWN__":
            print("ZEUS: Zeus shutting down.")
            break

        print("ZEUS:", response)


if __name__ == "__main__":
    main()