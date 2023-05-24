## Bitex Interview Task
### Task Description
1. Write a smart contract in Solidity that can store key-value pairs and retrieve values using keys. The smart contract should have functions for setting key-value pairs and getting values by keys. Both key and values are integers.
2. Set up a project to interact with the smart contract. Include necessary dependencies and configurations in the project.

3. Deploys the smart contract to a local Ethereum test network (e.g., Ganache, Hardhat, Anvil).
4. Use the ABI and contract address to create an instance of the smart contract.

5. Design and implement the API with the following endpoints: 
    POST /store: Stores a key-value pair in the smart contract.
    Request Body: `{ "key": "<key>", "value": "<value>" }`
    Response: { “success”: true, “message”: “Key-value pair stored successfully.” }
    GET `/retrieve?key=<key>:` Retrieves the value corresponding to the provided key from the smart contract.
    Response: { "key": "<key>", "value": "<value>" }

6. Provide documentation on how to set up and run the project

7. (Optional) Write unit tests for the API endpoints and smart contract functions.
  
### I wrote this project with python because I knew nothing about nodejs.
  
### Install
```
pip install -r requirements.txt
```

### Run
```
python app.py
```

### Endpoints
```
localhost:8545/store
localhost:8545/retrieve
```

### Test
You can use `hardhat test` with `npx hardhat test`
