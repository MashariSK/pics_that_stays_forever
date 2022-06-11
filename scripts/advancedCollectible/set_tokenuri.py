# token uri to show cute pics in opensea
# https://docs.openzeppelin.com/contracts/3.x/api/token/erc721#IERC721Metadata
from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_breed, get_account

# hardcoded, could create different json file and grab, but I don't like json
dog_metadata_dic = {
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=0-SHIBA_INU.json",
    "YOU": "https://ipfs.io/ipfs/QmaBQ8YsZqUiPWLyGs1oAFdavv6DApgfU5mnMM6wJVG1M8?filename=1-YOU.json"
}

def main():
    print(f"Working on {network.show_active()}")
    # use latest contract, modify as needed
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectibles} tokenIds")
    for token_id in range(number_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        # check if token url not alreday done
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, advanced_collectible, dog_metadata_dic[breed])
    


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button")