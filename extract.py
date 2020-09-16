import moviepy.editor as mp
clip =mp.VideoFileClip(r"video.mp4")
clip.audio.write_audiofile(r"audio.mp3")