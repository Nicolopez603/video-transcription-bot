import os
import ffmpeg
from pytube import YouTube

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download(output_path)
        print(f"Video downloaded successfully: {output_path}")
        return stream.default_filename
    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        return None

def extract_audio(video_path, audio_path):
    try:
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")

        if not os.path.exists(os.path.dirname(audio_path)):
            os.makedirs(os.path.dirname(audio_path))

        stream = ffmpeg.input(video_path)
        stream = ffmpeg.output(stream, audio_path, format='wav', acodec='pcm_s16le', ar=44100, ac=2)
        ffmpeg.run(stream)
        
        print(f"Audio extracted successfully: {audio_path}")
    except Exception as e:
        print(f"Error extracting audio: {str(e)}")