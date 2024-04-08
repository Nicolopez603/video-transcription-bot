import os
from pytube import YouTube
from utils.file_utils import create_directory

def download_youtube_video(url, output_path):
    create_directory(output_path)
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_filename = stream.default_filename
        video_path = os.path.join(output_path, video_filename)
        stream.download(output_path)
        return video_path
    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        return None