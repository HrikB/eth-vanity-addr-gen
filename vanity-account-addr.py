from eth_account import Account
from web3 import Web3
import os

def createAccount():
    priv_key = Web3.keccak(os.urandom(4096))
    acct = Account.from_key(priv_key);
    return {"priv": priv_key, "pub": acct.address}

def createVanityAddress(customString):
    i = 0
    while True:
        keys = createAccount()
        print(i, keys["pub"])
        i += 1
        if((customString.lower()) in keys["pub"][2:].lower()):
            return keys

keys = createVanityAddress("69420")
print("Address Found!")
print("You're address is:", keys["pub"])
print("You're private key is:", keys["priv"].hex())