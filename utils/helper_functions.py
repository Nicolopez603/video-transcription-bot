import os
from preprocessing.audio_extraction import download_youtube_video, extract_audio

def process_video(video_path, audio_directory):
    audio_filename = os.path.splitext(os.path.basename(video_path))[0] + '.wav'
    audio_path = os.path.join(audio_directory, audio_filename)
    extract_audio(video_path, audio_path)
    return audio_path

def process_youtube_url(url, video_directory, audio_directory):
    video_filename = download_youtube_video(url, video_directory)
    if video_filename:
        video_path = os.path.join(video_directory, video_filename)
        return process_video(video_path, audio_directory)
    return None