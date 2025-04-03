from block import Block
import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = []  # The list that stores the blockchain
        self.current_transactions = []  # List of transactions in the current block
        self.create_block(proof=1, previous_hash='0')  # Create the genesis block

    # Create a new block and add it to the chain
    def create_block(self, proof, previous_hash):
        block = Block(len(self.chain) + 1, previous_hash, time.time(), self.current_transactions, proof)
        self.current_transactions = []  # Reset the list of transactions for the next block
        self.chain.append(block)  # Add the block to the chain
        return block

    # Get the previous block in the chain
    def get_previous_block(self):
        return self.chain[-1]

    # Proof of work: find a new proof that satisfies the criteria
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            # Hash operation based on the formula: (new_proof^2 - previous_proof^2)
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            # Check if the first 4 characters of the hash are '0000'
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    # Add a new transaction to the list of current transactions
    def add_transaction(self, sender, receiver, amount):
        self.current_transactions.append({'sender': sender, 'receiver': receiver, 'amount': amount})
        return self.get_previous_block().index + 1  # Return the index of the block that will store the transaction

    # Validate the blockchain's integrity
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]

            # Check if the previous hash matches the hash of the previous block
            if block.previous_hash != previous_block.hash:
                return False

            previous_proof = previous_block.proof
            proof = block.proof

            # Check the proof of work: hash of (proof^2 - previous_proof^2) should start with '0000'
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False

            previous_block = block
            block_index += 1

        return True
