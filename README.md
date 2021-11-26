# Brownie ERC20

To modify the name and the symbol of your token, open [Token.sol](./contracts/Token.sol) and change `Token` and `TK` respectively.

To change the maximum supply, change the value of the `initial_supply` in [deploy.py](./scripts/deploy.py). Note that it will be in wei, meaning that you have to multiply it with 10<sup>18</sup>.

To deploy, use `brownie run scripts/deploy [--network network-name]` and your token will be deployed in a network you choose!