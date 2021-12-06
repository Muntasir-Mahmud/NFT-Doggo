from brownie import AdvanceCollectible, config, network
from brownie.network import account
from scripts.helpful_scripts import fund_with_link, get_account


def create():
    account = get_account()
    advanced_collectinle = AdvanceCollectible[-1]
    fund_with_link(advanced_collectinle.address)
    creation_tx = advanced_collectinle.createCollectible({"from": account})
    creation_tx.wait(1)
    print("Collectible created!!")


def main():
    create()
