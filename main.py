from generate_script import generate_script
from generate_voice import generate_voice
from fetch_visuals import fetch_video
from make_video import make_final_video

topic = "Benefits of Meditation"

print("Generating script...")
script = generate_script(topic)
print("Script:", script)

print("Generating voice...")
voice_path = generate_voice(script)

print("Downloading video...")
video_path = fetch_video("meditation")

print("Creating final video...")
make_final_video(video_path, voice_path)

print("✅ Video creation completed: final_video.mp4")
