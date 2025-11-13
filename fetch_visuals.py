import requests

with open("config/pexels_api_key.txt") as f:
    PEXELS_API_KEY = f.read().strip()

def fetch_video(query="nature", file_name="downloaded_video.mp4"):
    url = f"https://api.pexels.com/videos/search?query={query}&per_page=1"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if not data["videos"]:
        raise Exception("No videos found for this topic.")

    # Get the highest quality video link
    video_url = data["videos"][0]["video_files"][0]["link"]

    # Download the video
    video_data = requests.get(video_url, headers={'User-Agent': 'Mozilla/5.0'})
    with open(file_name, 'wb') as f:
        f.write(video_data.content)

    return file_name
