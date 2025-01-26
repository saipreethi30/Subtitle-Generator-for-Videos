# extract_audio.py
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio(video_file):
    """
    Extracts audio from a video file and saves it as a WAV file.
    """
    video = VideoFileClip(video_file)
    audio_file = video_file.replace('.mp4', '.wav')  # Change format if needed
    video.audio.write_audiofile(audio_file)
    video.close()  # Close the video file explicitly
    return audio_file
