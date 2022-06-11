from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract, get_account
from brownie import SimpleCollectible, network
import pytest
from scripts.advancedCollectible.deploy_and_create import deploy_and_create

def test_can_create_advanced_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Not in localblocakchain")
    advanced_collectible, creation_tx = deploy_and_create()
    requestId = creation_tx.events["requestedCollectible"]["requestId"]
    requester = creation_tx.events["requestedCollectible"]["requester"]
    eventy = creation_tx.events["requestedCollectible"]

    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, advanced_collectible.address, {"from": get_account()}
    )

    print("\n\n\n")
    print(f"token Counter: {advanced_collectible.tokenCounter()}")
    print(f"requestId: {requestId}")
    print(f"requester: {requester}")
    print("\n\n\n")
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3