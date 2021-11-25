from brownie import SampleToken, config, network

from scripts.helpful_scripts import get_account


def deploy():
    # 100 million max supply
    initial_supply = 100_000_000 * 10 ** 18

    SampleToken.deploy(
        initial_supply,
        {"from": get_account()},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )


def main():
    deploy()
