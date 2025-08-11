import speech_recognition as sr

def recognize_and_act():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio_mic = r.listen(source)
    try:
        text_mic = r.recognize_google(audio_mic)
        print("Microphone: " + text_mic)
        command = text_mic.lower()
        if "exit" in command or "quit" in command:
            print("Goodbye!")
            return False
        elif "light" in command and "on" in command:
            print("Turning the lights ON.")
        elif "light" in command and "off" in command:
            print("Turning the lights OFF.")
        elif "weather" in command:
            print("Checking weather...")
        elif "music" in command:
            print("Playing your favorite playlist.")
        else:
            print("Sorry, I don't know how to do that yet.")
    except sr.UnknownValueError:
        print("Microphone: Could not understand audio")
    except sr.RequestError as e:
        print(f"Microphone: Could not request results; {e}")
    return True

if __name__ == "__main__":
    while recognize_and_act():
        pass