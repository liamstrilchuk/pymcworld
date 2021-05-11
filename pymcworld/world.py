import time
import os
import datetime

from .option import Option
from random import randint
from .nbt import *
from .block import BlockList
from .shape import ShapeList
from .gamerules import GameRules
from .region import Region


class Logger:
	def log(self, message):
		print(f"{datetime.datetime.now().strftime('%m-%d-%y %H:%M:%S')} - {message}")


def cmod(n, base):
	"""
	Compute the modulus of a number like in languages such as C.
	
	:param n: the number to modulus
	:param base: the divisor
	"""

	return n - int(n / base) * base


class World:
	"""
	Creates a world. Allows users to set options for the world, set blocks,
	save the world to a folder, etc.
	"""

	def __init__(self, options=None) -> None:
		"""
		Creates the world.

		:param options: a dictionary which holds the world options.
		"""

		if options is None:
			options = {}

		self.gamerules = GameRules()
		self.options = {}
		self.world_loaded = False
		self.world_edited = False
		self.loaded_regions = {}
		self.seed = randint(1e8, 1e10)
		self.set_options(options)
		self.logger = Logger()
		self.regions = []
		self.blocks = BlockList
		self.shape = ShapeList(self)


	def set_block(self, x: int, y: int, z: int, block_type) -> bool:
		"""
		Set a single block. Returns true if the block was set, false otherwise.

		:param x: the x position of the block
		:param y: the y position of the block
		:param z: the z position of the block
		:param block_type: the block to set
		"""

		world_edited = True

		# check if position is out of bounds
		if y < 0 or y > 255:
			raise ValueError("Given position is out of world boundaries")

		# find the region coordinates
		regionX = x >> 9
		regionZ = z >> 9

		blockX = self.get_region_coord(x)
		blockZ = self.get_region_coord(z)

		# create the region if it doesn't already exist
		block_region = self.region_exists(regionX, regionZ)
		if not block_region:
			if self.world_loaded:
				region_path = f"r.{regionX}.{regionZ}.mca"
				if not region_path in self.loaded_regions:
					raise ValueError(
						"Given position is outside of loaded world boundaries"
					)

				region = Region(regionX, regionZ)
				region.load(self.loaded_regions[region_path])

			self.regions.append(Region(regionX, regionZ))
			block_region = self.regions[-1]

		# call the region set_block function
		return block_region.set_block(blockX, y, blockZ, block_type)


	def set_game_rule(self, name, value):
		"""
		Sets a gamerule.

		:param name: the name of the game rule
		:param value: the new value of the rule
		"""

		self.world_edited = True
		self.gamerules.set_rule(name, value)
	

	def get_block(self, x: int, y: int, z: int):
		"""
		Get the type of one block of the world.

		:param x: the x position of the block to get
		:param y: the y postiion of the block to get
		:param z: the z position of the block to get
		"""

		# check if the position is out of bounds
		if y < 0 or y > 255:
			raise ValueError("Given position is out of world boundaries")

		# find the coordinates of the region it is in
		regionX = x >> 9
		regionZ = z >> 9

		blockX = self.get_region_coord(x)
		blockZ = self.get_region_coord(z)

		# check if the region exists
		region = self.region_exists(regionX, regionZ)
		if not region:
			return self.blocks.AIR.get_block()

		return region.get_block(blockX, y, blockZ)


	def get_region_coord(self, pos):
		rc = cmod(pos, 512)

		return rc + 512 if rc < 0 else rc


	def save(self, folder_name: str) -> bool:
		"""
		Save the world to a folder. Returns true if successful, false otherwise.
		The files in the folder will be overwritten.

		Will create:
			- level.dat
			- region files
			- session.lock
		
		:param folder_name: the name of the folder to write the world to
		"""

		# check if the given folder name is the name of a file
		if os.path.isfile(folder_name):
			raise ValueError("Folder name is the name of a file")

		# check if the folder already exists
		if os.path.exists(folder_name):
			raise ValueError("Folder already exists")

		# set the world name
		self.options["LevelName"] = Option("LevelName", TAG_String, \
			foldername.split("/")[-1])

		# create the folder
		os.mkdir(folder_name)
		self.logger.log("world folder created")

		# create the region folder
		os.mkdir(f"{folder_name}/region")

		# create level.dat
		self.create_level_dat(f"{folder_name}/level.dat")
		self.logger.log("level.dat created")

		# create session.lock
		with open(f"{folder_name}/session.lock", "wb") as f:
			f.write(int(time.time() * 1000).to_bytes(8, "big"))

		# save every region
		for region in self.regions:
			filename = f"{folder_name}/region/r.{region.x}.{region.z}.mca"
			region.save(filename)
			self.logger.log(f"region file r.{region.x}.{region.z}.mca created")

		self.logger.log("all region files created, world is ready")

		return True


	def set_options(self, options: dict) -> None:
		"""
		Sets default options so the user doesn't have to worry about them.

		These options will be written to the level.dat file when the world
		is saved. Takes the user-defined arguments as a parameter.

		:param options: the options the user provides.
		"""

		# option presets
		self.options["GameType"] = Option("GameType", TAG_Byte, 1)
		self.options["LastPlayed"] = Option("LastPlayed", TAG_Long, \
				int(time.time() * 1000))
		self.options["LevelName"] = Option("LevelName", TAG_String, "world")
		self.options["MapFeatures"] = Option("MapFeatures", TAG_Byte, 0)
		self.options["RandomSeed"] = Option("RandomSeed", TAG_Long, self.seed)
		self.options["SpawnX"] = Option("SpawnX", TAG_Int, 0)
		self.options["SpawnY"] = Option("SpawnY", TAG_Int, 0)
		self.options["SpawnZ"] = Option("SpawnZ", TAG_Int, 0)
		self.options["allowCommands"] = Option("allowCommands", TAG_Byte, 1)
		self.options["version"] = Option("version", TAG_Int, 19133)
		self.options["initialized"] = Option("initialized", TAG_Byte, 1)
		self.options["DataVersion"] = Option("DataVersion", TAG_Int, 2586)

		# sets the options defined by the user
		for key in options:
			if not self.option_valid(key):
				raise ValueError(f"Option not valid: {key}")
			
			self.options[key].value = options[key]


	def option_valid(self, key: str) -> bool:
		"""
		Checks if an option is a possible option.
		Returns true if valid, false otherwise.

		:param key: the name of the option
		"""

		return key in Option.VALID_OPTIONS
		

	def create_level_dat(self, file_path: str) -> None:
		"""
		Creates the level.dat file, using an NBT library.

		:param file_path: the file path to write to.
		"""

		# create the nbt file
		nbtfile = NBTFile()
		
		# create the root tag
		root_tag = TAG_Compound()
		root_tag.name = "Data"

		# add the options
		for op in self.options:
			root_tag.tags.append(self.options[op].create_tag())

		# create the world generator, to make a void world
		root_tag.tags.append(self.create_generator())
		
		# create data pack tag
		data_pack_tag = TAG_Compound()
		data_pack_tag.name = "DataPacks"

		disabled_list = TAG_List(name="Disabled", type=TAG_String)
		enabled_list = TAG_List(name="Enabled", type=TAG_String)
		enabled_list.tags.append(TAG_String(value="vanilla"))

		data_pack_tag.tags.extend([disabled_list, enabled_list])
		root_tag.tags.append(data_pack_tag)

		# create dragon fight tag
		dragon_fight = TAG_Compound()
		dragon_fight.name = "DragonFight"

		gateway_tag = TAG_List(name="Gateways", type=TAG_Int)

		for i in range(20):
			gateway_tag.tags.append(TAG_Int(value=i))

		dragon_fight.tags.extend([
			TAG_Byte(name="DragonKilled", value=1),
			TAG_Byte(name="PreviouslyKilled", value=1),
			gateway_tag
		])

		root_tag.tags.append(dragon_fight)

		# add the gamerules to the level.dat
		gamerule_tag = TAG_Compound()
		gamerule_tag.name = "GameRules"

		for rule in self.gamerules.rules:
			str_tag = TAG_String(name=rule["name"], value=rule["value"])
			gamerule_tag.tags.append(str_tag)

		root_tag.tags.append(gamerule_tag)

		nbtfile.tags.append(root_tag)
		nbtfile.write_file(file_path)

	
	def region_exists(self, x, z):
		"""
		Checks if a region exists at the given coordinates.

		:param x: the x position to check
		:param z: the z position to check
		"""

		for region in self.regions:
			if region.x == x and region.z == z:
				return region

		return False


	def load(self, world_folder):
		"""
		Load a world from a given folder.
		Loads each region file as needed, overwriting the original file.

		:param world_folder: the path to the folder containing the world.
		"""

		# check if the level.dat exists
		level_dat = os.path.join(world_folder, "level.dat")
		if not os.path.exists(level_dat):
			raise ValueError(f"Cannot find file at path {level_dat}")

		# check if the session.lock exists
		session_lock = os.path.join(world_folder, "session.lock")
		if not os.path.exists(session_lock):
			raise ValueError(f"Cannot find file at path {session_lock}")

		# check if the world region data exists
		region_dir = os.path.join(world_folder, "region")
		if not os.path.exists(region_dir):
			raise ValueError(f"Cannot find folder at path {region_dir}")

		# check if region files are present
		region_list = os.listdir(region_dir)
		if len(region_list) == 0:
			raise ValueError(f"No region files found in world folder")

		self.world_loaded = True
		self.loaded_regions = {
			v: os.path.join(region_dir, v) for v in region_list
		}


	def create_generator(self):
		"""
		Creates the generator options for the level.dat.
		Takes no arguments, returns TAG_Compound.

		Format:

		WorldGenSettings: TAG_Compound
			dimensions: TAG_Compound
				minecraft:overworld: TAG_Compound
					generator: TAG_Compound
						settings: TAG_Compound
							structures: TAG_Compound
								structures: TAG_Compound
									minecraft:village: TAG_Compound
										salt: TAG_Int
										separation: TAG_Int
										spacing: TAG_Int
								stronghold: TAG_Compound
									count: TAG_Int
									distance: TAG_Int
									spread: TAG_Int
							layers: TAG_List(TAG_Compound)
							lakes: TAG_Byte
							features: TAG_Byte
							biome: TAG_String
						type: TAG_String
					type: TAG_String
			bonus_chest: TAG_Byte
			generate_features: TAG_Byte
			seed: TAG_Long
		"""

		# create the generation settings
		generator_tag = TAG_Compound()
		generator_tag.name = "WorldGenSettings"

		# add basic tags
		generator_tag.tags.extend([
			TAG_Byte(name="bonus_chest", value=0),
			TAG_Byte(name="generate_features", value=0),
			TAG_Long(name="seed", value=self.seed)
		])

		# create the nested compound tags needed
		dimension_tag = TAG_Compound()
		dimension_tag.name = "dimensions"

		overworld_tag = TAG_Compound()
		overworld_tag.name = "minecraft:overworld"

		overworld_gen_tag = TAG_Compound()
		overworld_gen_tag.name = "generator"

		settings_tag = TAG_Compound()
		settings_tag.name = "settings"

		structures_tag = TAG_Compound()
		structures_tag.name = "structures"

		stronghold_tag = TAG_Compound()
		stronghold_tag.name = "stronghold"

		stronghold_tag.tags.extend([
			TAG_Int(name="count", value=128),
			TAG_Int(name="distance", value=32),
			TAG_Int(name="spread", value=3)
		])

		nested_structures = TAG_Compound()
		nested_structures.name = "structures"

		village_tag = TAG_Compound()
		village_tag.name = "minecraft:village"

		village_tag.tags.extend([
			TAG_Int(name="salt", value=randint(1e7, 1e9)),
			TAG_Int(name="separation", value=8),
			TAG_Int(name="spacing", value=32)
		])

		nested_structures.tags.append(village_tag)

		structures_tag.tags.extend([
			stronghold_tag,
			nested_structures
		])

		# add default values
		settings_tag.tags.extend([
			TAG_String(name="biome", value="minecraft:plains"),
			TAG_Byte(name="features", value=0),
			TAG_Byte(name="lakes", value=0),
			TAG_List(name="layers", type=TAG_Compound),
			structures_tag
		])

		# append each layer
		overworld_gen_tag.tags.extend([
			settings_tag,
			TAG_String(name="type", value="minecraft:flat")
		])

		overworld_tag.tags.extend([
			overworld_gen_tag,
			TAG_String(name="type", value="minecraft:overworld")
		])

		dimension_tag.tags.append(overworld_tag)
		
		end_tag = TAG_Compound()
		end_tag.name = "minecraft:the_end"
		
		end_gen_tag = TAG_Compound()
		end_gen_tag.name = "generator"
		
		end_biome_source = TAG_Compound()
		end_biome_source.name = "biome_source"
		
		end_biome_source.tags.extend([
			TAG_String(name="type", value="minecraft:the_end"),
			TAG_Long(name="seed", value=self.seed)
		])
		
		end_gen_tag.tags.extend([
			end_biome_source,
			TAG_Long(name="seed", value=self.seed),
			TAG_String(name="settings", value="minecraft:end"),
			TAG_String(name="type", value="minecraft:noise")
		])
		
		end_tag.tags.extend([
			end_gen_tag,
			TAG_String(name="type", value="minecraft:the_end")
		])
		
		nether_tag = TAG_Compound()
		nether_tag.name = "minecraft:the_nether"
		
		nether_gen_tag = TAG_Compound()
		nether_gen_tag.name = "generator"
		
		nether_biome_source = TAG_Compound()
		nether_biome_source.name = "biome_source"
		
		nether_biome_source.tags.extend([
			TAG_String(name="type", value="minecraft:multi_noise"),
			TAG_Long(name="seed", value=self.seed),
			TAG_String(name="preset", value="minecraft:nether")
		])
		
		nether_gen_tag.tags.extend([
			nether_biome_source,
			TAG_Long(name="seed", value=self.seed),
			TAG_String(name="settings", value="minecraft:nether"),
			TAG_String(name="type", value="minecraft:noise")
		])
		
		nether_tag.tags.extend([
			nether_gen_tag,
			TAG_String(name="type", value="minecraft:the_nether")
		])
		
		dimension_tag.tags.extend([end_tag, nether_tag])
		generator_tag.tags.append(dimension_tag)

		return generator_tag

