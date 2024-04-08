from utils.helper_functions import process_youtube_url
from asr.speech_recognition import transcribe_audio
from summarization.text_summarization import generate_summary

def main():
    video_directory = 'data/input/videos'
    audio_directory = 'data/output/audio'
    youtube_url = 'https://www.youtube.com/watch?v=VIDEO_ID'

    audio_path = process_youtube_url(youtube_url, video_directory, audio_directory)
    if audio_path:
        transcript = transcribe_audio(audio_path)
        if transcript:
            summary = generate_summary(transcript)
            if summary:
                print(f"Video Summary: {summary}")

if __name__ == '__main__':
    main()