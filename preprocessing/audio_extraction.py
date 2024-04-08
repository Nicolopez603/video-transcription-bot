import os
import ffmpeg

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