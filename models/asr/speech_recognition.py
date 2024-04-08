import speech_recognition as sr
import speech_recognition as sr

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        transcript = recognizer.recognize_sphinx(audio)
        return transcript
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from speech recognition service; {str(e)}")

    return None

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        transcript = recognizer.recognize_sphinx(audio)
        print(f"Transcription: {transcript}")
        return transcript
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from speech recognition service; {str(e)}")

    return None
