from .chunk import Chunk
from math import ceil
from .block import BlockList
import time


def cmod(n, base):
	"""
	Compute the modulus of a number like in languages such as C.
	
	:param n: the number to modulus
	:param base: the divisor
	"""

	return n - int(n / base) * base


class Region:
	"""
	A region class which defines an area of 32x32 chunks, or
	512x256x512 blocks. This makes up a single .mca file.
	"""

	def __init__(self, x, z):
		"""
		Creates the region class.

		:param x: the x position of the region
		:param z: the z position of the region
		"""

		self.chunks = self.create_chunks()
		self.x = x
		self.z = z

	
	def create_chunks(self):
		"""
		Creates the chunks for the region, setting them all to 0.
		"""

		chunks = []

		for x in range(32):
			chunks.append([])

			for z in range(32):
				chunks[len(chunks) - 1].append(0)

		return chunks


	def set_block(self, x, y, z, block):
		"""
		Sets a single block. This is called by the world's set_block.

		:param x: the x position of the block to set
		:param y: the y position of the block to set
		:param z: the z position of the block to set
		:param block: the block to set, has name and block properties
		"""

		# find the position of the chunk within the region
		chunkX = z // 16
		chunkZ = x // 16

		# if the chunk doesn't already exist, create it
		if not self.chunks[chunkX][chunkZ]:
			self.chunks[chunkX][chunkZ] = Chunk(
				z // 16,
				x // 16
			)

		return self.chunks[chunkX][chunkZ].set_block(
			cmod(z, 16), y, cmod(x, 16), block
		)

	
	def get_block(self, x, y, z):
		"""
		Get a single block in the region. Called by the World class.

		:param x: the x position of the block to get
		:param y: the y position of the block to get
		:param z: the z position of the block to get
		"""

		# find the position of the chunk within the region
		chunkX = z // 16
		chunkZ = x // 16

		# check if the chunk exists
		if not self.chunks[chunkX][chunkZ]:
			return BlockList.AIR.get_block()

		return self.chunks[chunkX][chunkZ].get_block(
			cmod(z, 16), y, cmod(x, 16)
		)


	def save(self, filename):
		"""
		Save the region to a file. The filename takes the form r.x.z.mca.
		The file format is specified in the Minecraft Wiki.

		:param filename: the filename to save the region to.
		"""

		# first we have to get the compressed NBT data from the chunks
		data = self.create_chunks()

		for x in range(32):
			for z in range(32):
				if self.chunks[x][z]:
					data[x][z] = self.chunks[x][z].get_compressed_nbt()
		
		# create the headers (chunk locations and timestamps)
		location_header = b""
		timestamp_header = b""
		all_data = b""
		current_offset = 2

		for x in range(32):
			for z in range(32):
				# add the time in epoch seconds to the timestamp header
				timestamp_header += int(time.time()).to_bytes(4, "big")

				# if the chunk is not initialised
				if data[x][z] == 0:
					location_header += b"\x00\x00\x00\x00"
					continue

				# get the chunk size in 4 KB sectors
				chunk_size = ceil((len(data) + 5) / 4096)

				# add the chunk offset and chunk size to the location header
				location_header += current_offset.to_bytes(3, "big")
				location_header += chunk_size.to_bytes(1, "big")

				# add the chunk size to the offset
				current_offset += chunk_size

				# add the chunk data to the data string
				all_data += data[x][z]

		with open(filename, "wb") as f:
			f.write(location_header + timestamp_header + all_data)

