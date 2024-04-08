import os
from utils.video_utils import download_youtube_video
from utils.file_utils import delete_file
from preprocessing.audio_extraction import extract_audio
from asr.speech_recognition import transcribe_audio
from summarization.text_summarization import generate_summary

def process_youtube_video(url):
    video_directory = 'data/input/videos'
    audio_directory = 'data/output/audio'

    video_path = download_youtube_video(url, video_directory)
    if video_path:
        audio_filename = os.path.splitext(os.path.basename(video_path))[0] + '.wav'
        audio_path = os.path.join(audio_directory, audio_filename)
        audio_path = extract_audio(video_path, audio_path)
        if audio_path:
            transcript = transcribe_audio(audio_path)
            if transcript:
                summary = generate_summary(transcript)
                delete_file(video_path)
                delete_file(audio_path)
                return summary
    return None

def main():
    youtube_url = 'https://www.youtube.com/watch?v=VIDEO_ID'
    summary = process_youtube_video(youtube_url)
    if summary:
        print(f"Video Summary: {summary}")
    else:
        print("Failed to generate video summary.")

if __name__ == '__main__':
    main()