import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio_mic = r.listen(source)
    try:
        text_mic = r.recognize_google(audio_mic)
        print("Microphone: " + text_mic)
        return text_mic.lower()
    except sr.UnknownValueError:
        print("Microphone: Could not understand audio")
    except sr.RequestError as e:
        print(f"Microphone: Could not request results; {e}")
    return None