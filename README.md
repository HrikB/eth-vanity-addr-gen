# Ethereum Vanity Address Generators

## Overview
The two python programs allow a user to create vanity addresses for either accounts or smart contracts on the Ethereum Blockchain. 



### ACCOUNTS
Use 'vanity-account-addr.py'
Nothing is needed to generate the account. After simply inputting the desired prefix, the program will find the user a corresponing private key.

### CONTRACTS
Use 'vanity-contr-addr.py'
Generating contracts with vanity addresses is significantly more complicated so follow along closely:
1. First compile the contract for which you would like a custom address. After compilation, retrieve the contract's byte code. This can be done on Remix IDE
2. Copy the bytecode and paste it into the pair of quotes after 'hex' on line 6 in CreateVanityContract.sol
3. Additionally, use the keccak-256 hash on the bytecode; we will need this later
4. Now take CreateVanityContract.sol, compile it, then deploy it (all possible on Remix IDE). This is the deploying address
5. Replace 'deploying_addr' on line 7 of the program with this deploying address
6. Replace 'bytecode_hash' on line 8 with the keccak-256 hash of the bytecode from earlier
7. Finally, replace 'prefix' on line 9 with your desired prefix. Remember that the only valid characters in your prefix are 0-9 and A-F. Also note that the longer your desired prefix, the longer it will take to find.
8. After a while, the program will output a salt for an address with your provided paramters.
9. Use that salt to call the 'createContract' function on the CreateVanityContract.sol contract. If you deployed on Remix, you can simply go to the Deployed Contracts section.
10. After the contract call, you can simply go to the etherscan address of your CreateVanityContract.sol contract address, view the Internal Transactions and follow the trail.
11. Now you have deployed a contract to your desired address, and since you have the ABI via Remix compilation, you can interact with it as you please.
