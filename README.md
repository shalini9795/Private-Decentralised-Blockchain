# Tech Stack Used

UI is made in Streamlit - main.py

Persistance is done in mongodb using the Pymongo package

The APIs are created using Flask


# Private-Decentralised-Blockchain

Blockchain technology is used for a de centralized network enabled verification of KYC documents. 

The customer does this details upload only to the first bank the customer is going to. Which means that he/she does not have
any bank accounts previously or had done any KYC verification previously.

The uploaded files get stored in the bank’s local database. The banks maintain these databases only for the
temporary storage of the customer’s files.

## Mining a block
It is the process of finding a nonce which satisfies the HASH restrictions. In this architecture, the government is
assumed to be the one’s building and maintaining the blockchain. Once the documents are received by the
government, they mine a block with the requisites.

## Proof of Work
While mining a block, once the hashkey is generated, the hashkey is verified for the predetermined sequence.
If the condition is satisfied, the proof of work is complete. If not, the hashkey is again generated.

SHA 512 has 128 characters as compared to SHA 256 with 64 characters.
The reason for choosing SHA-512:
● It is faster than SHA-256 on 64-bit machines is that has 37.5% less rounds per byte (80 rounds operating
on 128 byte blocks) compared to SHA- 256 (64 rounds operating on 64 byte blocks)
● It is more secure than SHA 256

## Adding data to block
Once the proof of work is completed successfully, the verified data documents are added to the block.

## Adding to the blockchain
Once the block is created successfully, the block will be added by the government to the blockchain.

## Broadcasting the updated blockchain
The updated blockchain is now being broadcast to all the nodes (banks) in the network. This is done by replacing
the blockchain of all the nodes with the new blockchain along with the added block.
If a new bank wants to get integrated to the blockchain, then an add node module is used to add the node to
the blockchain network.

## Retrieving details from Blockchain
Details are retrieved based on the unique key identifier in the data.

## Saving the transactions in Pymongo

`def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:5011/")

    mydb = myclient["KYCDatabase"]
    print("database created")
    return mydb

def saveDB(name,aadhar,pan,address,phone):
    mydb=get_database()
    mycol = mydb["customers"]
    mydict = {"name":name , "address":address,"phone":phone,"aadhar":aadhar,"pan":pan}
    x = mycol.insert_one(mydict)
    print(x)'
    
## Adding Transaction block
```@app.route('/mine_block', methods = ['GET'])
def mine_block():
    receiver_data = request.get_json()
    print(receiver_data,"receiver")
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    #receiver_data = collection.insert_one(data)
    print("receiver_data",receiver_data)
    receiver_data={"name": " Sudarshanam",
 "aadhar": "2678789012344567",
 "pan": "234123456",
  "address": "123",
   "phone": "7259645662"}
    blockchain.add_transaction(name=receiver_data['name'],aadhar=receiver_data['aadhar'],pan=receiver_data['pan'],
                               address=receiver_data['address'],phone=receiver_data['phone'])
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Added the block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions': block['transactions']}
    return jsonify(response), 200```
