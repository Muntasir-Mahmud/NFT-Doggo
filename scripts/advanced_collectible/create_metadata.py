from pathlib import Path

import requests
from brownie import AdvanceCollectible, network
from metadata.sample_metadata import metadata_template
from scripts.helpful_scripts import get_breed


def main():
    advanced_collectible = AdvanceCollectible[-2]
    print(advanced_collectible.address)
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"{number_of_advanced_collectibles} collectibles are created!!")
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to override!")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectible_metadata["name"] = breed,
            collectible_metadata["description"] = f"An adorable {breed} pup!"
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
            image_uri = upload_to_ipfs(image_path)
            # collectible_metadata["image_uri"] = 


def upload_to_ipfs(file_path):
    with Path(file_path).open("rb") as fp: # rb = binary
        image_binary = fp.read()
        # Upload image...
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        file_name = file_path.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={file_name}"
        print(image_uri)
        return image_uri
