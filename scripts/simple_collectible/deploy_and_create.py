from scripts.helpful_scripts import get_account, SimpleCollectible, OPENSEA_URL

sample_token_uri = "https://ipfs.io/ipfs/QmVthzYxEHmjMdkhsCqVPUzurAtJAKW88HtapFnetBTHVX?filename=st-bernard.json"


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Now on {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    )
    print("Please wait for 20mins then refresh metadata.")
    return simple_collectible


def main():
    deploy_and_create()
