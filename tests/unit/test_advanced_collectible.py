import pytest
from brownie import network
from brownie.network import account
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import (LOCAL_BLOCKCHAIN_ENVIRONMENTS,
                                     get_account, get_contract)


def test_can_create_advanced_collectible():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    # Act
    advanced_collectible, creation_tracsaction = deploy_and_create()
    requestId = creation_tracsaction.events["reqestedCollectible"]["requestId"]
    random_number = 786
    get_contract("vrf_coordinator").callBackWithRandomness(requestId, random_number, advanced_collectible.address, {"from": get_account()})
    # Assert
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3
