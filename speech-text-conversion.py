import speech_recognition as sr

r = sr.Recognizer() # Initialize recognizer

# Recognize speech from microphone
with sr.Microphone() as source:
    print("Say something!")
    audio_mic = r.listen(source)
    try:
        text_mic = r.recognize_google(audio_mic)
        print("Microphone: " + text_mic)
    except sr.UnknownValueError:
        print("Microphone: Could not understand audio")
    except sr.RequestError as e:
        print(f"Microphone: Could not request results; {e}")