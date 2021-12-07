import pytest
from brownie import network
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)


def test_can_create_advanced_collectible():
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for integration testing")
    # Act
    advanced_collectible, creation_tracsaction = deploy_and_create()
    # Assert
    assert advanced_collectible.tokenCounter() == 1
