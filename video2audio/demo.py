from moviepy.editor import *
path = "test.mp4"
video = VideoFileClip(path)
audio = video.audio
audio.write_audiofile("test.mp3")
