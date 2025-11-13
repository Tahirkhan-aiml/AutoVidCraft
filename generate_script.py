import openai

with open("config/openai_api_key.txt") as f:
    openai.api_key = f.read().strip()

def generate_script(topic):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Write a short, engaging video script (about 100 words) on this topic."},
            {"role": "user", "content": topic}
        ]
    )
    return response.choices[0].message.content
