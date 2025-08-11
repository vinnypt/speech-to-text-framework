from intent import get_intent
from actions import intent_actions
from voice import recognize_speech

def main():
    while True:
        command = recognize_speech()
        if not command:
            continue

        if "exit" in command or "quit" in command:
            print("Goodbye!")
            break

        intent = get_intent(command)
        print(f"Detected intent: {intent}")

        if intent and intent in intent_actions:
            intent_actions[intent]()
        else:
            print("Sorry, I don't know how to do that yet.")

if __name__ == "__main__":
    main()