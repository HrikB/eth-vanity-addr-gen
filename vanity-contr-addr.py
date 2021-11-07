from web3 import Web3

#CREATE2 Opcode Formula: keccak256(0xff ++ deployingAddr ++ salt ++ keccak256(bytecode))[26:]

#FILL THESE OUT
#---------------------------------------------------------------------------------------------------------------------------------#
deploying_addr = '0AB387A71cB8A18952C60fA2d0998082a568a86A'#The address of the CREATE2 smart contract
bytecode_hash = '3dd18c918f41583af2495ac76600d039b410609ee62b0d717fc4f6745e5ed38a' #keccak256 hex hash of the bytecode of the contract you want to deploy; Get byte code from remix and use online keccak256 hasher like https://emn178.github.io/online-tools/keccak_256.html. Make to set input type to hex
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