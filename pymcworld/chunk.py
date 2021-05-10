from .nbt import *
from .section import Section
from .block import BlockList
import zlib
import io


class Long_Array(TAG_Long_Array):
	def __init__(self, name=""):
		super().__init__(name)


	def update_fmt(self, length):
		self.fmt = Struct(">" + str(length) + "Q")


class Chunk:
	"""
	Defines a single chunk of 16x256x16.
	1024 of these chunks make up a region.
	"""

	def __init__(self, x, z):
		"""
		Creates the chunk.

		:param x: the x position of the chunk
		:param z: the z position of the chunk
		"""

		self.x = x
		self.z = z
		self.sections = {}
	
	
	def set_block(self, x, y, z, block):
		"""
		Set a single block within the chunk.

		:param x: the x position of the block to set
		:param y: the y position of the block to set
		:param z: the z position of the block to set
		:param block: the type of block to set
		"""

		# find the section that contains the block
		sectionY = y >> 4

		if not sectionY in self.sections:
			self.sections[sectionY] = Section(self.x, sectionY, self.z)

		return self.sections[sectionY].set_block(x, y % 16, z, block)


	def get_block(self, x, y, z):
		"""
		Get a single block within the chunk.

		:param x: the x position of the block to get
		:param y: the y position of the block to get
		:param z: the z position of the block to get
		"""

		# find the section that contains the block
		sectionY = y >> 4

		# if the section does not exist, return air
		if not sectionY in self.sections:
			return BlockList.AIR

		return self.sections[sectionY].get_block(x, y % 16, z)


	def get_compressed_nbt(self):
		"""
		Takes the chunk data and puts it into an NBTFile object.
		Takes no parameters, returns NBTFile buffer.
		"""

		# create and name the file
		nbtfile = NBTFile()
		nbtfile.name = ""

		# create the root tag
		root_tag = TAG_Compound()
		root_tag.name = "Level"

		# create the necessary tags
		section_list = TAG_List(name="Sections", type=TAG_Compound)

		# add the sections
		for y in self.sections:
			section_list.tags.append(self.get_section_nbt(y))

		root_tag.tags.append(section_list)
		root_tag.tags.append(TAG_Int(name="xPos", value=self.x))
		root_tag.tags.append(TAG_Int(name="zPos", value=self.z))
		root_tag.tags.append(TAG_String(name="Status", value="full"))
		root_tag.tags.append(TAG_Byte(name="TerrainPopulated", value=1))
		root_tag.tags.append(TAG_Byte(name="LightPopulated", value=1))
		root_tag.tags.append(TAG_Byte(name="V", value=1))

		# write the root tag to the NBT file object
		nbtfile.tags.append(root_tag)

		# data version for 1.16.5
		nbtfile.tags.append(TAG_Int(name="DataVersion", value=2586))

		# create buffer
		bytes_buffer = io.BytesIO()

		# write to the buffer using NBT library
		nbtfile.write_file(buffer=bytes_buffer)

		# convert BytesIO to string
		bytes_buffer.seek(0)
		byte_str = bytes_buffer.read()

		# return the compressed data
		return self.pad_chunk_data(zlib.compress(byte_str))


	def get_section_nbt(self, y):
		"""
		Gets the NBT data for one section of the chunk.

		:param y: the y position of the section
		"""

		palette_tag = TAG_List(name="Palette", type=TAG_Compound)

		# create the blocks in the palette
		for block in self.sections[y].palette.blocks:
			block_tag = TAG_Compound()
			block_tag.tags.append(
				TAG_String(name="Name", value=block["name"])
			)

			# add each block's properties, if they exist
			if len(block["properties"]) > 0:
				properties_tag = TAG_Compound()
				properties_tag.name = "Properties"

				for prop in block["properties"]:
					properties_tag.tags.append(
						TAG_String(name=prop, value=block["properties"][prop])
					)

				block_tag.tags.append(properties_tag)

			# add the block to the palette
			palette_tag.tags.append(block_tag)

		# get an array of longs as block data
		block_data = self.sections[y].get_block_data()
		block_data_tag = Long_Array(name="BlockStates")
		block_data_tag.value = block_data

		section_tag = TAG_Compound()

		section_tag.tags.append(palette_tag)
		section_tag.tags.append(block_data_tag)
		section_tag.tags.append(TAG_Byte(name="Y", value=y))
		
		return section_tag


	def pad_chunk_data(self, data):
		"""
		Adds 5 bytes at the start describing the chunk, and pads the data
		with 0s so the length is a multiple of 4096.

		:param data: the binary string of compressed data
		"""

		data_length = len(data)
		new_length = data_length + 5
		padding = b"\x00" * (4096 - (new_length % 4096))

		return data_length.to_bytes(4, "big") + b"\x02" + data + padding


	def load(self, data):
		"""
		Load the chunk from the given data.

		:param data: the chunk data
		"""

		pass

