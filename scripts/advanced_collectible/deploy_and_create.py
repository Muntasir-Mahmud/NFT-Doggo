from brownie import AdvanceCollectible, config, network
from scripts.helpful_scripts import (OPENSEA_URL, fund_with_link, get_account,
                                     get_contract)


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvanceCollectible.deploy(
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get(
            "verify", False
        ),
    )
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New token has been created!!")
    return advanced_collectible, creating_tx

def main():
    deploy_and_create()
