#!/usr/bin/env python

import hashlib
import datetime

class Block():

	def __init__(self, data, number, previousHash):
		self.data = data
		self.number = number
		self.previousHash = previousHash
		self.timestamp = datetime.datetime.now()
		self.hash = self.createHash()

	@staticmethod
	def createGenesisBlock():
		return Block('Genesis Block', 0, '0')

	def createHash(self):
		headerBinary = (
			str(self.data) +
			str(self.number) +
			str(self.previousHash) +
			str(self.timestamp)
		).encode()

		innerHash = hashlib.sha256(headerBinary).hexdigest().encode()
		outerHash = hashlib.sha256(innerHash).hexdigest()

		return outerHash

class BlockChain():

	def __init__(self):
		self.chain = [Block.createGenesisBlock()]

	def add(self, data):
		self.chain.append(
			Block(data, self.chain[-1].number + 1,  self.chain[-1].hash)
		)

	def block(self, number):
		return self.chain[number]

	def list(self):
		for block in self.chain:
			print(f'''
Block Number: {block.number}
Block Hash: {block.hash}
Block Data: {block.data}
Block timestap: {block.timestamp}
Previous Block: {block.previousHash}
			''')

blockchain = BlockChain()

def main():
	blockchain.add('This is a test block 1')
	blockchain.add('This is a test block 2')
	#blockchain.list()

	print(blockchain.block(1).hash)

if __name__ == "__main__":
	main()
