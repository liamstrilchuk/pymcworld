from .nbt import *

class Option:
	"""
	Defines an option for the level.dat.
	"""

	def __init__(self, name: str, option_type, value: str):
		"""
		Creates the option.

		:param name: the name of the option.
		:param option_type: the type of the option.
		:param value: the option's value.
		"""

		self.name = name
		self.option_type = option_type
		self.value = value

	def create_tag(self):
		"""
		Creates the NBT tag and returns it. Takes no parameters.
		"""

		# check if it is a special type (eg. list)
		if self.option_type == TAG_Compound or \
			self.option_type == TAG_List or \
			self.option_type == TAG_Int_Array or \
			self.option_type == TAG_Long_Array:
			return False

		# create the tag
		tag = self.option_type(name=self.name, value=self.value)

		return tag

	"""
	List of valid options.
	"""
	VALID_OPTIONS = [
		"GameType", # the game mode - 0 survival, 1 creative, etc.
		"LevelName", # the world name
		"RandomSeed", # the world seed
		"SpawnX", # default spawn X
		"SpawnY", # default spawn Y
		"SpawnZ", # default spawn Z
		"allowCommands" # 1 for commands allowed, 0 for not allowed
	]

	# defines the possible tags for the options
	TAG_END = 0
	TAG_BYTE = 1
	TAG_SHORT = 2
	TAG_INT = 3
	TAG_LONG = 4
	TAG_FLOAT = 5
	TAG_DOUBLE = 6
	TAG_BYTE_ARRAY = 7
	TAG_STRING = 8
	TAG_LIST = 9
	TAG_COMPOUND = 10
	TAG_INT_ARRAY = 11
	TAG_LONG_ARRAY = 12

