import math


class ShapeList:
	"""
	A list of shapes used by the world.
	"""

	def __init__(self, world):
		"""
		Creates the list.

		:param world: the world to write to
		"""

		self.world = world
	
	
	def sphere(self, x, y, z, radius, block, full=False):
		"""
		Creates a sphere.

		:param x: the center x position of the sphere
		:param y: the center y position of the sphere
		:param z: the center z position of the sphere
		:param radius: the radius of the sphere
		:param block: the type of block the sphere is made of
		:param full: if the sphere should be filled
		"""

		# make sure the min/max y positions are in the world
		if y - radius < 0 or y + radius > 255:
			raise ValueError("Shape position is out of world boundaries")

		# cycle through all possible positions
		for sx in range(-radius, radius + 1):
			for sy in range(-radius, radius + 1):
				for sz in range(-radius, radius + 1):
					dist = math.sqrt(
						(sx + 0.5) * (sx + 0.5) +
						(sy + 0.5) * (sy + 0.5) +
						(sz + 0.5) * (sz + 0.5)
					)

					# if the distance from the center is the radius
					side_width = 0 if full else radius - 1

					if dist >= side_width and dist <= radius:
						self.world.set_block(
							x + sx,
							y + sy,
							z + sz,
							block
						)


	def cube(self, x, y, z, width, height, length, block):
		"""
		Creates a cube.

		:param x: the bottom left corner x position of the cube
		:param y: the bottom left corner y position of the cube
		:param z: the bottom left corner z position of the cube
		:param width: the width of the cube
		:param height: the height of the cube
		:param length: the length of the cube
		:param block: the material the cube should be
		"""

		for cx in range(width):
			for cy in range(height):
				for cz in range(length):
					self.world.set_block(
						x + cx,
						y + cy,
						z + cz,
						block
					)

