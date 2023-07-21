#web3

from web3 import Web3,HTTPProvider
import json
artifact="../build/contracts/voting.json"

def connect_with_blockchain(wallet): #from which wallet we have to connect with blockchain
    #blockchain server
    blockchainServer='http://127.0.0.1:7545'
    #web3 object connects with server
    web3=Web3(HTTPProvider(blockchainServer)) #object web3 is ready to connect with blockchain server
    #accessing abi, address
    with open(artifact) as f:  #f is a file . open a file
        artifact_json=json.load(f) #load json file
        contract_abi=artifact_json['abi']  #
        contract_address=artifact_json['networks']['5777']['address']
        #from which wallet
        web3.eth.defaultAccount=wallet
        #contract instance to which wallet has to 
        contract=web3.eth.contract(      
            abi=contract_abi,  #paasing contract abi
            address=contract_address  #paasing contract address
        )
        return(contract,web3)


contract, web3=connect_with_blockchain('0xF1d95bC236Ff9f9D4E061d36526b5A23B89ee200') #wallet address
#tx_hash=contract.functions.castVote(1).transact()   
#web3.eth.waitForTransactionReceipt(tx_hash)
#print('vote casted')
_votes=contract.functions.displayVotes().call()
print(_votes) #read data from blockchain which shows
