from .palette import Palette
from .block import Air


class Section:
	"""
	Defines a single section of 16x16x16 blocks. There are 16 sections
	in a chunk.
	"""
	
	def __init__(self, x, y, z):
		"""
		Creates the section and the variables it needs.

		:param x: the x position of the section's chunk
		:param y: the y position of the section, from 0 to 16
		:param z: the z position of the section's chunk
		"""

		self.x = x
		self.y = y
		self.z = z

		self.palette = Palette()
		
		# add air to the palette
		self.palette.blocks.append(Air().get_block())
		self.palette.block_hashes.append("{}minecraft:air")
		self.palette.block_amounts.append(4096)

		self.blocks = [0] * 4096

	
	def set_block(self, x, y, z, block):
		"""
		Set a single block to the section. Adds the block to the
		palette if it is not already in there.

		:param x: the x position of the block to set
		:param y: the y position of the block to set
		:param z: the z position of the block to set
		:param block: the block type to set
		"""

		# remove the old block from the palette if it was the only instance
		is_sub = self.palette.subtract_block(self.palette.blocks[self.blocks[
			self.get_block_offset(x, y, z)
		]])

		if is_sub is not None:
			for i in range(len(self.blocks)):
				if self.blocks[i] > is_sub:
					self.blocks[i] -= 1

		# add the block to the palette
		block_index = self.palette.block_index(block.get_block())

		# update the section's block array
		self.blocks[self.get_block_offset(
			x, y, z
		)] = block_index

		return True


	def get_block(self, x, y, z):
		"""
		Get a single block within the section. Returns a dictionary with
		the name and properties of the block.

		:param x: the x position of the block to set
		:param y: the y position of the block to set
		:param z: the z position of the block to set
		"""

		# return the block within the palette
		block = self.palette.blocks[self.blocks[
			self.get_block_offset(x, y, z)
		]]

		return {
			"name": block["name"],
			"properties": block["properties"]
		}


	def get_block_offset(self, x, y, z):
		"""
		Get the offset of a certain block in the self.blocks array.

		:param x: the x position of the block relative to the section x
		:param y: the y position of the block relative to the section y
		:param z: the z position of the block relative to the section z
		"""

		return (x * (16 ** 0)) + (y * (16 ** 1)) + (z * (16 ** 2))


	def get_block_data(self):
		"""
		Create the blockdata for saving chunks. Each block takes up a minimum
		of 4 bits, but takes as many bits as needed to represent the biggest
		block index value in the palette. Takes no parameters, returns an
		array of longs (8 bytes each).
		"""

		long_array = [0]

		# the number of bits needed for each block
		bits_per_block = max(len(self.palette.blocks).bit_length(), 4)

		# the number of bits remaining in the current long
		bits_remaining = 64
		current_bit = 0

		# set the bits for each block
		# according to Minecraft Wiki, blocks are arranged in YZX format
		for y in range(16):
			for x in range(16):
				for z in range(16):
					# check if there are not enough bits in the long
					if bits_remaining < bits_per_block:
						long_array.append(0)
						bits_remaining = 64
						current_bit = 0

					# add the block value to the long
					long_array[-1] += self.blocks[
						self.get_block_offset(x, y, z)
					] << current_bit
					current_bit += bits_per_block
					bits_remaining -= bits_per_block

		return long_array
	
