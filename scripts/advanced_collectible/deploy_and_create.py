from brownie import AdvancedCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_account


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy({"from": account})


def main():
    deploy_and_create()
