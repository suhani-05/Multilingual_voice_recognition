from modules.audio_handler import record_audio
from modules.speech_to_text import recognize_speech

if __name__ == "__main__":
    # Record audio
    audio = record_audio()

    # Convert speech to text
    text = recognize_speech(audio)

    if text:
        print(f"Recognized Text: {text}")
    else:
        print("Sorry, couldn't recognize the speech.")
