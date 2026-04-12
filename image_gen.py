import requests
from PIL import Image
import io
import time
import os

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_image(topic: str):
    prompt = f"Simple educational diagram explaining {topic}, clean illustration, labeled diagram"

    for i in range(5):
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

        print("STATUS:", response.status_code)

        if response.status_code == 200:
            return Image.open(io.BytesIO(response.content))

        elif response.status_code == 503:
            print("Model loading... retrying")
            time.sleep(5)

        else:
            print("ERROR:", response.text)
            return None

    return None