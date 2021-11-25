# Brownie ERC20

To modify the name and the symbol of your token, open [SampleToken.sol](./contracts/SampleToken.sol) and change `SampleToken` and `ST` respectively.

To change the maximum supply, change the value of the `initial_supply` in [deploy_token.py](./scripts/deploy_token.py). Note that it will be in wei, meaning that you have to multiply it with 10<sup>18</sup>.

To deploy, use `brownie run scripts/deploy_token [--network network-name]` and your token will be deployed in a network you choose!