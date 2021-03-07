import json


class Palette:
	"""
	A palette of blocks for one section of a chunk. Each palette includes
	one instance of each unique block in the chunk.
	"""

	def __init__(self):
		"""
		Create an empty palette. Takes no arguments.
		"""

		self.blocks = []
		self.block_hashes = []
		self.block_amounts = []
	

	def block_index(self, block, add=True):
		"""
		Find the index of a block in the palette. Used for storing the blocks
		in the section.

		:param block: the block to search for
		:param add: whether to add the block if it is not found
		"""

		# create the unique hash of the block
		block_hash = self.generate_block_hash(block)

		# check if it is already in the palette
		if block_hash not in self.block_hashes and add:
			self.block_hashes.append(block_hash)
			self.blocks.append(block)
			self.block_amounts.append(1)
		elif block_hash not in self.block_hashes and not add:
			return -1
		elif block_hash in self.block_hashes and add:
			self.block_amounts[self.block_hashes.index(block_hash)] += 1

		return self.block_hashes.index(block_hash)


	def subtract_block(self, block):
		"""
		Remove a block from the palette if it no longer has any instances
		in the section. Returns the index if it is removed, None otherwise.

		:param block: the block to check
		"""

		block_hash = self.generate_block_hash(block)

		if block_hash not in self.block_hashes:
			return None

		index = self.block_hashes.index(block_hash)

		self.block_amounts[index] -= 1

		# if the block no longer has any instances
		if self.block_amounts[index] == 0:
			del self.block_amounts[index]
			del self.block_hashes[index]
			del self.blocks[index]
			return index

		return None


	def generate_block_hash(self, block):
		"""
		Generate a unique hash for each block. Includes the properties & name.

		:param block: the block to create the hash for
		"""

		return json.dumps(
			block["properties"],
			separators=(",", ":")
			) + block["name"]

