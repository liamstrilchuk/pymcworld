class Structure:
	"""
	Creates a user-defined structure. Allows users to add sub-structures
	and blocks, along with logic.
	"""

	def __init__(self, x, y, z):
		"""
		Create the structure. Takes the position as parameters.

		:param x: the x position of the structure
		:param y: the y position of the structure
		:param z: the z position of the structure
		"""

		self.x = x
		self.y = y
		self.z = z
		self.blocks = {}

	
	def create(self):
		"""
		The default create function for the structure.
		"""

		pass


	def set_block(self, x, y, z, block):
		"""
		Set a single block in the structure.

		:param x: the block's x position
		:param y: the block's y position
		:param z: the block's z position
		:param block: the type of block to set
		"""

		# check if the block has the required properties
		if isinstance(block, dict):
			if not "name" in block or not "properties" in block:
				raise ValueError("Block does not have reqired values")
		else:
			try:
				properties = dir(block)
				if not "name" in properties or not "properties" in properties:
					raise ValueError("Block does not have required values")
			except Exception as err:
				raise ValueError("Block does not have required values")

		# find the position
		r_x = x
		r_y = y
		r_z = z

		# add the block to the structure's block dictionary
		if not r_x in self.blocks:
			self.blocks[r_x] = {}

		if not r_y in self.blocks[r_x]:
			self.blocks[r_x][r_y] = {}

		if not r_z in self.blocks[r_x][r_y]:
			self.blocks[r_x][r_y][r_z] = None

		self.blocks[r_x][r_y][r_z] = block

	
	def add_structure(self, structure, x, y, z, rotation):
		"""
		Add a sub-structure's blocks to this structure. Returns nothing.

		:param structure: the structure to add, must have create function
		:param x: the x position to add the structure at
		:param y: the y position to add the structure at
		:param z: the z position to add the structure at
		:param rotation: the rotation of the structure, in radians
		"""

		# create an instance of the structure
		ins = structure(x, y, z)
		ins.create(rotation)

		# go through all the blocks in the instance
		for b_x in ins.blocks:
			for b_y in ins.blocks[x]:
				for b_z in ins.blocks[x][y]:
					# find the position relative to this position
					adjusted_x = x
					adjusted_y = y
					adjusted_z = z

					if ins.blocks[x][y][z] is None:
						continue

					# place the block in the self.blocks dictionary
					if not adjusted_x in self.blocks:
						self.blocks[adjusted_x] = {}

					if not adjusted_y in self.blocks[adjusted_x]:
						self.blocks[adjusted_x][adjusted_y] = {}

					self.blocks[adjusted_x][adjusted_y][adjusted_z] = \
						ins.blocks[b_x][b_y][b_z]



	def place(self, rotation, world):
		"""
		Places the structure. Takes rotation and world as parameters.

		:param rotation: the rotation to place the structure at, in radians
		:param world: the world class to use
		"""

		for x in self.blocks:
			for y in self.blocks[x]:
				for z in self.blocks[x][y]:
					if self.blocks[x][y][z] is None:
						continue

					# find the new position after rotating
					rotated_x = x
					rotated_z = z

					# use the world to set the block
					world.set_block(
						rotated_x,
						y,
						rotated_z,
						self.blocks[x][y][z]
					)

