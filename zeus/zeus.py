import datetime

def greet():
    print("ZEUS ONLINE")
    print("I am Zeus.")
    print("I am ready.")

def think(message):
    text = message.lower()
    if "hello" in text or "hi" in text:
        return "Greetings. Zeus is listening."
    if "time" in text:
        now = datetime.datetime.now()
        return "The time is " + now.strftime("%H:%M")
    if "who are you" in text:
        return "I am Zeus. Your digital agent."
    if "exit" in text or "quit" in text:
        return None
    return "I hear you. Give me a moment to become wiser."

def main():
    greet()
    while True:
        message = input("\nKeith: ")
        response = think(message)
        if response is None:
            print("Zeus: Until next time.")
            break
        print("Zeus:", response)

if __name__ == "__main__":
    main()
