from flask import Flask, request, jsonify
from web3 import Web3
from web3.contract import ConciseContract

# connect to the local network
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# set the contract address and ABI
contract_address = '0x0000000000000000000000000000000000000000'

# insert your ABI here
abi = [
        abi= [
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "key",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "set",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "key",
        "type": "uint256"
      }
    ],
    "name": "get",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]

# create an instance of the contract
contract_instance= w3.eth.contract(
    address=contract_address,
    abi=abi,
    ContractFactoryClass=ConciseContract
)


app= Flask(__name__)

# define the store endpoint to store key-value pairs in the smart contract


@ app.route('/store', methods=['POST'])
def store():
    key= request.json['key']
    value= request.json['value']

    # call the setValue function on the smart contract
    tx_hash= contract_instance.setValue(key, value)

    return jsonify({
        'success': True,
        'message': 'Key-value pair stored successfully.'
    })

# define the retrieve endpoint to retrieve a value using a key from the smart contract


@ app.route('/retrieve')
def retrieve():
    key= int(request.args.get('key'))

    # call the getValue function on the smart contract
    value= contract_instance.getValue(key)

    return jsonify({
        'key': key,
        'value': value
    })


if __name__ == '__main__':
    app.run(debug=True)
