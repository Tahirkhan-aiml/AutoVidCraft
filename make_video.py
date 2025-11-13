from moviepy import VideoFileClip, AudioFileClip

def make_final_video(video_path, audio_path, output_path="final_video.mp4"):
    video = VideoFileClip(video_path).subclip(0, AudioFileClip(audio_path).duration)
    video = video.set_audio(AudioFileClip(audio_path))
    video.write_videofile(output_path, fps=24)
