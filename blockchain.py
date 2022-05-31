import requests
import hashlib
import json
from time import time

class Blockchain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

    # Create genesis block
    self.new_block(previous_hash=1, proof=100)

  def new_block(self, proof, previous_hash=None):
    """
    Creates and adds new block to chain
    :param proof: <int> proof given by Proof of Work algorithm
    :param previous_hash: (Optional) <str> Hash of previous block
    :return: <dict> New Block
    """

    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'proof': proof,
      'previous_hash': previous_hash or self.hash(self.chain(-1))
    }

    # Reset current list of transactions
    self.current_transactions = []

    self.chain.append(block)
    return block

  def new_transaction(self, sender, recipient, amount):
    # Adds transaction to list of transactions
    """
    Creates a new transaction
    :param sender: <str> Address of sender
    :param recipient: <str> Address of recipient
    :param amount: <int> Amount
    :return: <int> Index of block that will hold this transaction
    """

    self.current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount,
    })

    return self.last_block['index'] + 1

  @staticmethod
  def hash(block):
    """
    Creates a Sha-256 hash of block
    :param block: <dict> block
    :return: <str>
    """

    # Ensures dictionary is ordered
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

  @property
  def last_block(self):
    # Returns last block in chain
    pass

