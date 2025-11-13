import requests
import tempfile
import pygame
import os

with open("config/elevenlabs_api_key.txt") as f:
    ELEVENLABS_API_KEY = f.read().strip()

def generate_voice(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"  # Replace with your preferred voice ID

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "voice_settings": {"stability": 0.4, "similarity_boost": 0.6}
    }

    response = requests.post(url, headers=headers, json=data)
    # print("response", response.status_code, response.content )

    if response.status_code != 200:
        raise Exception("Voice generation failed")

    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_audio.write(response.content)
    temp_audio.close()

    return temp_audio.name
