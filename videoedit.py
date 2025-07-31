from moviepy.editor import *

def render_video(images, voice_file, captions_file):
    clips = [ImageClip(img).set_duration(5) for img in images]
    video = concatenate_videoclips(clips, method="compose")
    audio = AudioFileClip(voice_file)
    video = video.set_audio(audio)
    output_path = "final_video.mp4"
    video.write_videofile(output_path, fps=24)
    return output_path

