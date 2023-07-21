from flask import Flask,request
from blockchain import *
#create an object
api=Flask(__name__)

@api.route('/')  #define  a basic route
def home():  #define a function
    return('API Server is Online')


#create api for casting vote
@api.route('/castvote',methods=['get','post']) #get api call method
def castvote():
  id=request.args.get('id') #API value stored in id  ...0
  wallet=request.args.get('wallet')
  print(id)
  try:
    contract,web3=connect_with_blockchain(wallet)
    tx_hash=contract.functions.castVote(int(id)).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return('You have voted for {0}'.format(id)) #API respond method.
  except:
      return('you have already voted')

#create api for displaying votes
@api.route('/displayvotes',methods=['get','post'])
def displayvotes():
    wallet=request.args.get('wallet')
    contract,web3=connect_with_blockchain(wallet)
    _votes=contract.functions.displayVotes().call()
    return(str(_votes))

#create api for creating an account - signup
@api.route('/signup',methods=['get','post'])
def signup():
    username=request.args.get('username')
    password=request.args.get('password')
    print(username,password)
    try:
        contract,web3=connect_with_blockchain_register(username)
        tx_hash=contract.functions.signup(username,int(password)).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        return('Account Created')
    except:
        return('Account Exist')

#create api for login
@api.route('/login',methods=['get','post'])
def login():
    username=request.args.get('username')
    password=request.args.get('password')
    print(username,password)
    contract,web3=connect_with_blockchain_register(username)
    loginstatus=contract.functions.login(username,int(password)).call()
    return(str(loginstatus))

if __name__=="__main__":
    api.run(
      host='0.0.0.0',
      port=5001,
       debug=True
    )
