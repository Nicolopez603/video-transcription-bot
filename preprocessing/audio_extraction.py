import os
import ffmpeg
from utils.file_utils import create_directory

def extract_audio(video_path, audio_path):
    create_directory(os.path.dirname(audio_path))
    try:
        stream = ffmpeg.input(video_path)
        stream = ffmpeg.output(stream, audio_path, format='wav', acodec='pcm_s16le', ar=44100, ac=2)
        ffmpeg.run(stream, overwrite_output=True)
        return audio_path
    except Exception as e:
        print(f"Error extracting audio: {str(e)}")
        return None