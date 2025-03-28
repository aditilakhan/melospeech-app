import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)
    try:
        print("You said: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Error with recognition service")
