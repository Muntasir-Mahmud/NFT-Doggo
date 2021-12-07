from brownie import AdvanceCollectible
from scripts.helpful_scripts import get_breed


def main():
    advanced_collectible = AdvanceCollectible[-2]
    print(advanced_collectible.address)
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"{number_of_advanced_collectibles} collectibles are created!!")
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
