import speech_recognition as sr

def record_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening now...")

        try:
            audio = recognizer.listen(source)
            return audio
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return None
