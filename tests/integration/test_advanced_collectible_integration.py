from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract, get_account
from brownie import AdvancedCollectible, network
import pytest, time
from scripts.advancedCollectible.deploy_and_create import deploy_and_create

def test_can_create_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")

    advanced_collectible, creation_tx = deploy_and_create()
    time.sleep(60)

    # print("\n\n\n")
    # print(f"token Counter: {advanced_collectible.tokenCounter()}")
    # print(f"requestId: {requestId}")
    # print(f"requester: {requester}")
    # print("\n\n\n")
    print(advanced_collectible.tokenCounter())
    assert advanced_collectible.tokenCounter() == 1
    # assert advanced_collectible.tokenIdToBreed(0) == random_number % 3