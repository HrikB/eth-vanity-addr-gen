from web3 import Web3

#CREATE2 Opcode Formula: keccak256(0xff ++ deployingAddr ++ salt ++ keccak256(bytecode))[26:]

#FILL THESE OUT
#---------------------------------------------------------------------------------------------------------------------------------#
deploying_addr = '21C2713e850E7A6477C52F4621360a3956AafFc3'#The address of the CREATE2 smart contract
bytecode_hash = 'fe614dc399b15172dd21827b03b40d938c21e1ee92a68e9e9460d35f2b2f21ce' #keccak256 hex hash of the bytecode of the contract you want to deploy; Get byte code from remix and use online keccak256 hasher like https://emn178.github.io/online-tools/keccak_256.html. Make to set input type to hex
prefix = "BBBB" #This is case insensitive
#---------------------------------------------------------------------------------------------------------------------------------#

def searchForCreate2Seed(deploying_addr, bytecode_hash, prefix):
    pref_addr = '0xff' + deploying_addr  # ff + deploying_addr
    for i in range(72057594037927936):
        #convert i to hex
        saltInBytes = '0x{0:064X}'.format(i);


        stringToHash = pref_addr + saltInBytes[2:] + bytecode_hash
        potenial_addr = Web3.keccak(hexstr=stringToHash).hex()[26:]
        print(i, saltInBytes, potenial_addr)
        if(potenial_addr.startswith(prefix.lower())):
            print("Your salt for contract address", potenial_addr, "is", saltInBytes)
            break;

searchForCreate2Seed(deploying_addr, bytecode_hash, prefix);