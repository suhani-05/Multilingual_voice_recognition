import speech_recognition as sr

def recognize_speech(audio):
    recognizer = sr.Recognizer()

    if audio is None:
        return None

    try:
        print("Processing speech...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition; {e}")
        return None
