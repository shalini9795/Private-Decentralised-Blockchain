# Tech Stack Used

UI is made in Streamlit - UI.py
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


