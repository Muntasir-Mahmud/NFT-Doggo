import os
from pathlib import Path

import requests

PINATA_BASE_URL = "https://api.pinata.cloud"
END_POINT = "/pinning/pinFileToIPFS"

file_path = "./img/pug.png"
file_name = file_path.split("/")[-1:][0]

print(os.getenv("PINATA_API_KEY"))

headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SERECT_KEY")
}

def main():
    with Path(file_path).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + END_POINT, files={"file": (file_name, image_binary)},
            headers=headers
        )
        print(response.json())
