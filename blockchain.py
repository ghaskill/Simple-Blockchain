class Blockchain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

  def new_block(self):
    # Creates and adds new block to chain
    pass

  def new_transaction(self):
    # Adds transaction to list of transactions
    pass

  @staticmethod
  def hash(block):
    # Hashes a block
    pass

  @property
  def last_block(self):
    # Returns last block in chain
    pass

