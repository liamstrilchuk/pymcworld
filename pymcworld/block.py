from random import randint


class Block:
	"""
	A block class. Contains the block type and properties.
	"""

	def __init__(self, name, properties):
		"""
		:param block_type: the namespaced block type.
		:param properties: a dictionary of properties for the block.
		"""

		self.name = name
		self.properties = properties
	
	
	def get_block(self):
		"""
		Gets the block's name and properties.
		"""

		return {"name": self.name, "properties": self.properties}


class BlockPalette:
	"""
	Allows a random choice of two or more blocks.
	"""

	def __init__(self, block_array):
		"""
		Creates the block palette. Takes an array of possible blocks as an
		argument.

		:param block_array: the list of possible blocks
		"""

		if len(block_array) < 1:
			return ValueError("Must have at least one block in the list")

		self.block_array = block_array

	
	def get_block(self):
		"""
		Get a random block from the palette.
		"""

		return self.block_array[
			randint(0, len(self.block_array) - 1)].get_block()


class AcaciaButton(Block):
	def __init__(self):
		super().__init__("acacia_button", {})


class AcaciaDoor(Block):
	def __init__(self):
		super().__init__("acacia_door", {})


class AcaciaFence(Block):
	def __init__(self):
		super().__init__("acacia_fence", {})


class AcaciaFenceGate(Block):
	def __init__(self):
		super().__init__("acacia_fence_gate", {})


class AcaciaLeaves(Block):
	def __init__(self):
		super().__init__("acacia_leaves", {})


class AcaciaLog(Block):
	def __init__(self):
		super().__init__("acacia_log", {})


class AcaciaPlanks(Block):
	def __init__(self):
		super().__init__("acacia_planks", {})


class AcaciaPressurePlate(Block):
	def __init__(self):
		super().__init__("acacia_pressure_plate", {})


class AcaciaSign(Block):
	def __init__(self):
		super().__init__("acacia_sign", {})


class AcaciaSlab(Block):
	def __init__(self):
		super().__init__("acacia_slab", {})


class AcaciaStairs(Block):
	def __init__(self):
		super().__init__("acacia_stairs", {})


class AcaciaTrapdoor(Block):
	def __init__(self):
		super().__init__("acacia_trapdoor", {})


class AcaciaWood(Block):
	def __init__(self):
		super().__init__("acacia_wood", {})


class ActivatorRail(Block):
	def __init__(self):
		super().__init__("activator_rail", {})


class Air(Block):
	def __init__(self):
		super().__init__("air", {})


class AncientDebris(Block):
	def __init__(self):
		super().__init__("ancient_debris", {})


class Andesite(Block):
	def __init__(self):
		super().__init__("andesite", {})


class AndesiteSlab(Block):
	def __init__(self):
		super().__init__("andesite_slab", {})


class AndesiteStairs(Block):
	def __init__(self):
		super().__init__("andesite_stairs", {})


class AndesiteWall(Block):
	def __init__(self):
		super().__init__("andesite_wall", {})


class Anvil(Block):
	def __init__(self):
		super().__init__("anvil", {})


class Barrel(Block):
	def __init__(self):
		super().__init__("barrel", {})


class Basalt(Block):
	def __init__(self):
		super().__init__("basalt", {})


class Barrier(Block):
	def __init__(self):
		super().__init__("barrier", {})


class Beacon(Block):
	def __init__(self):
		super().__init__("beacon", {})


class Bedrock(Block):
	def __init__(self):
		super().__init__("bedrock", {})


class BeeNest(Block):
	def __init__(self):
		super().__init__("bee_nest", {})


class Beehive(Block):
	def __init__(self):
		super().__init__("beehive", {})


class Bell(Block):
	def __init__(self):
		super().__init__("bell", {})


class BirchButton(Block):
	def __init__(self):
		super().__init__("birch_button", {})


class BirchDoor(Block):
	def __init__(self):
		super().__init__("birch_door", {})


class BirchFence(Block):
	def __init__(self):
		super().__init__("birch_fence", {})


class BirchFenceGate(Block):
	def __init__(self):
		super().__init__("birch_fence_gate", {})


class BirchLeaves(Block):
	def __init__(self):
		super().__init__("birch_leaves", {})


class BirchLog(Block):
	def __init__(self):
		super().__init__("birch_log", {})


class BirchPlanks(Block):
	def __init__(self):
		super().__init__("birch_planks", {})


class BirchPressurePlate(Block):
	def __init__(self):
		super().__init__("birch_pressure_plate", {})


class BirchSign(Block):
	def __init__(self):
		super().__init__("birch_sign", {})


class BirchSlab(Block):
	def __init__(self):
		super().__init__("birch_slab", {})


class BirchStairs(Block):
	def __init__(self):
		super().__init__("birch_stairs", {})


class BirchTrapdoor(Block):
	def __init__(self):
		super().__init__("birch_trapdoor", {})


class BirchWood(Block):
	def __init__(self):
		super().__init__("birch_wood", {})


class BlackConcrete(Block):
	def __init__(self):
		super().__init__("black_concrete", {})


class BlackConcretePowder(Block):
	def __init__(self):
		super().__init__("black_concrete_powder", {})


class BlackGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("black_glazed_terracotta", {})


class BlackShulkerBox(Block):
	def __init__(self):
		super().__init__("black_shulker_box", {})


class BlackStainedGlass(Block):
	def __init__(self):
		super().__init__("black_stained_glass", {})


class BlackStainedGlassPane(Block):
	def __init__(self):
		super().__init__("black_stained_glass_pane", {})


class BlackTerracotta(Block):
	def __init__(self):
		super().__init__("black_terracotta", {})


class BlackWool(Block):
	def __init__(self):
		super().__init__("black_wool", {})


class Blackstone(Block):
	def __init__(self):
		super().__init__("blackstone", {})


class BlackstoneSlab(Block):
	def __init__(self):
		super().__init__("blackstone_slab", {})


class BlackstoneStairs(Block):
	def __init__(self):
		super().__init__("blackstone_stairs", {})


class BlackstoneWall(Block):
	def __init__(self):
		super().__init__("blackstone_wall", {})


class BlastFurnace(Block):
	def __init__(self):
		super().__init__("blast_furnace", {})


class BlueConcrete(Block):
	def __init__(self):
		super().__init__("blue_concrete", {})


class BlueConcretePowder(Block):
	def __init__(self):
		super().__init__("blue_concrete_powder", {})


class BlueGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("blue_glazed_terracotta", {})


class BlueIce(Block):
	def __init__(self):
		super().__init__("blue_ice", {})


class BlueShulkerBox(Block):
	def __init__(self):
		super().__init__("blue_shulker_box", {})


class BlueStainedGlass(Block):
	def __init__(self):
		super().__init__("blue_stained_glass", {})


class BlueStainedGlassPane(Block):
	def __init__(self):
		super().__init__("blue_stained_glass_pane", {})


class BlueTerracotta(Block):
	def __init__(self):
		super().__init__("blue_terracotta", {})


class BlueWool(Block):
	def __init__(self):
		super().__init__("blue_wool", {})


class BoneBlock(Block):
	def __init__(self):
		super().__init__("bone_block", {})


class Bookshelf(Block):
	def __init__(self):
		super().__init__("bookshelf", {})


class BrainCoralBlock(Block):
	def __init__(self):
		super().__init__("brain_coral_block", {})


class BrickSlab(Block):
	def __init__(self):
		super().__init__("brick_slab", {})


class BrickStairs(Block):
	def __init__(self):
		super().__init__("brick_stairs", {})


class BrickWall(Block):
	def __init__(self):
		super().__init__("brick_wall", {})


class Bricks(Block):
	def __init__(self):
		super().__init__("bricks", {})


class BrownConcrete(Block):
	def __init__(self):
		super().__init__("brown_concrete", {})


class BrownConcretePowder(Block):
	def __init__(self):
		super().__init__("brown_concrete_powder", {})


class BrownGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("brown_glazed_terracotta", {})


class BrownMushroomBlock(Block):
	def __init__(self):
		super().__init__("brown_mushroom_block", {})


class BrownShulkerBox(Block):
	def __init__(self):
		super().__init__("brown_shulker_box", {})


class BrownStainedGlass(Block):
	def __init__(self):
		super().__init__("brown_stained_glass", {})


class BrownStainedGlassPane(Block):
	def __init__(self):
		super().__init__("brown_stained_glass_pane", {})


class BrownTerracotta(Block):
	def __init__(self):
		super().__init__("brown_terracotta", {})


class BrownWool(Block):
	def __init__(self):
		super().__init__("brown_wool", {})


class BubbleCoralBlock(Block):
	def __init__(self):
		super().__init__("bubble_coral_block", {})


class Cactus(Block):
	def __init__(self):
		super().__init__("cactus", {})


class CartographyTable(Block):
	def __init__(self):
		super().__init__("cartography_table", {})


class CarvedPumpkin(Block):
	def __init__(self):
		super().__init__("carved_pumpkin", {})


class Cauldron(Block):
	def __init__(self):
		super().__init__("cauldron", {})


class Chain(Block):
	def __init__(self):
		super().__init__("chain", {})


class ChainCommandBlock(Block):
	def __init__(self):
		super().__init__("chain_command_block", {})


class Chest(Block):
	def __init__(self):
		super().__init__("chest", {})


class ChippedAnvil(Block):
	def __init__(self):
		super().__init__("chipped_anvil", {})


class ChiseledNetherBricks(Block):
	def __init__(self):
		super().__init__("chiseled_nether_bricks", {})


class ChiseledPolishedBlackstone(Block):
	def __init__(self):
		super().__init__("chiseled_polished_blackstone", {})


class ChiseledQuartzBlock(Block):
	def __init__(self):
		super().__init__("chiseled_quartz_block", {})


class ChiseledRedSandstone(Block):
	def __init__(self):
		super().__init__("chiseled_red_sandstone", {})


class ChiseledSandstone(Block):
	def __init__(self):
		super().__init__("chiseled_sandstone", {})


class ChiseledStoneBricks(Block):
	def __init__(self):
		super().__init__("chiseled_stone_bricks", {})


class ChorusFlower(Block):
	def __init__(self):
		super().__init__("chorus_flower", {})


class ChorusPlant(Block):
	def __init__(self):
		super().__init__("chorus_plant", {})


class Clay(Block):
	def __init__(self):
		super().__init__("clay", {})


class CoalBlock(Block):
	def __init__(self):
		super().__init__("coal_block", {})


class CoalOre(Block):
	def __init__(self):
		super().__init__("coal_ore", {})


class CoarseDirt(Block):
	def __init__(self):
		super().__init__("coarse_dirt", {})


class Cobblestone(Block):
	def __init__(self):
		super().__init__("cobblestone", {})


class CobblestoneSlab(Block):
	def __init__(self):
		super().__init__("cobblestone_slab", {})


class CobblestoneStairs(Block):
	def __init__(self):
		super().__init__("cobblestone_stairs", {})


class CobblestoneWall(Block):
	def __init__(self):
		super().__init__("cobblestone_wall", {})


class Cobweb(Block):
	def __init__(self):
		super().__init__("cobweb", {})


class CommandBlock(Block):
	def __init__(self):
		super().__init__("command_block", {})


class Comparator(Block):
	def __init__(self):
		super().__init__("comparator", {})


class Composter(Block):
	def __init__(self):
		super().__init__("composter", {})


class Conduit(Block):
	def __init__(self):
		super().__init__("conduit", {})


class CrackedNetherBricks(Block):
	def __init__(self):
		super().__init__("cracked_nether_bricks", {})


class CrackedPolishedBlackstoneBricks(Block):
	def __init__(self):
		super().__init__("cracked_polished_blackstone_bricks", {})


class CrackedStoneBricks(Block):
	def __init__(self):
		super().__init__("cracked_stone_bricks", {})


class CraftingTable(Block):
	def __init__(self):
		super().__init__("crafting_table", {})


class CrimsonButton(Block):
	def __init__(self):
		super().__init__("crimson_button", {})


class CrimsonDoor(Block):
	def __init__(self):
		super().__init__("crimson_door", {})


class CrimsonFence(Block):
	def __init__(self):
		super().__init__("crimson_fence", {})


class CrimsonFenceGate(Block):
	def __init__(self):
		super().__init__("crimson_fence_gate", {})


class CrimsonHyphae(Block):
	def __init__(self):
		super().__init__("crimson_hyphae", {})


class CrimsonNylium(Block):
	def __init__(self):
		super().__init__("crimson_nylium", {})


class CrimsonPlanks(Block):
	def __init__(self):
		super().__init__("crimson_planks", {})


class CrimsonPressurePlate(Block):
	def __init__(self):
		super().__init__("crimson_pressure_plate", {})


class CrimsonSign(Block):
	def __init__(self):
		super().__init__("crimson_sign", {})


class CrimsonSlab(Block):
	def __init__(self):
		super().__init__("crimson_slab", {})


class CrimsonStairs(Block):
	def __init__(self):
		super().__init__("crimson_stairs", {})


class CrimsonStem(Block):
	def __init__(self):
		super().__init__("crimson_stem", {})


class CrimsonTrapdoor(Block):
	def __init__(self):
		super().__init__("crimson_trapdoor", {})


class CryingObsidian(Block):
	def __init__(self):
		super().__init__("crying_obsidian", {})


class CutRedSandstone(Block):
	def __init__(self):
		super().__init__("cut_red_sandstone", {})


class CutRedSandstoneSlab(Block):
	def __init__(self):
		super().__init__("cut_red_sandstone_slab", {})


class CutSandstone(Block):
	def __init__(self):
		super().__init__("cut_sandstone", {})


class CutSandstoneSlab(Block):
	def __init__(self):
		super().__init__("cut_sandstone_slab", {})


class CyanConcrete(Block):
	def __init__(self):
		super().__init__("cyan_concrete", {})


class CyanConcretePowder(Block):
	def __init__(self):
		super().__init__("cyan_concrete_powder", {})


class CyanGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("cyan_glazed_terracotta", {})


class CyanShulkerBox(Block):
	def __init__(self):
		super().__init__("cyan_shulker_box", {})


class CyanStainedGlass(Block):
	def __init__(self):
		super().__init__("cyan_stained_glass", {})


class CyanStainedGlassPane(Block):
	def __init__(self):
		super().__init__("cyan_stained_glass_pane", {})


class CyanTerracotta(Block):
	def __init__(self):
		super().__init__("cyan_terracotta", {})


class CyanWool(Block):
	def __init__(self):
		super().__init__("cyan_wool", {})


class DamagedAnvil(Block):
	def __init__(self):
		super().__init__("damaged_anvil", {})


class DarkOakButton(Block):
	def __init__(self):
		super().__init__("dark_oak_button", {})


class DarkOakFence(Block):
	def __init__(self):
		super().__init__("dark_oak_fence", {})


class DarkOakFenceGate(Block):
	def __init__(self):
		super().__init__("dark_oak_fence_gate", {})


class DarkOakLeaves(Block):
	def __init__(self):
		super().__init__("dark_oak_leaves", {})


class DarkOakLog(Block):
	def __init__(self):
		super().__init__("dark_oak_log", {})


class DarkOakPlanks(Block):
	def __init__(self):
		super().__init__("dark_oak_planks", {})


class DarkOakPressurePlate(Block):
	def __init__(self):
		super().__init__("dark_oak_pressure_plate", {})


class DarkOakSign(Block):
	def __init__(self):
		super().__init__("dark_oak_sign", {})


class DarkOakSlab(Block):
	def __init__(self):
		super().__init__("dark_oak_slab", {})


class DarkOakStairs(Block):
	def __init__(self):
		super().__init__("dark_oak_stairs", {})


class DarkOakTrapdoor(Block):
	def __init__(self):
		super().__init__("dark_oak_trapdoor", {})


class DarkOakWood(Block):
	def __init__(self):
		super().__init__("dark_oak_wood", {})


class DarkPrismarine(Block):
	def __init__(self):
		super().__init__("dark_prismarine", {})


class DarkPrismarineSlab(Block):
	def __init__(self):
		super().__init__("dark_prismarine_slab", {})


class DarkPrismarineStairs(Block):
	def __init__(self):
		super().__init__("dark_prismarine_stairs", {})


class DaylightDetector(Block):
	def __init__(self):
		super().__init__("daylight_detector", {})


class DeadBrainCoralBlock(Block):
	def __init__(self):
		super().__init__("dead_brain_coral_block", {})


class DeadBubbleCoralBlock(Block):
	def __init__(self):
		super().__init__("dead_bubble_coral_block", {})


class DeadFireCoralBlock(Block):
	def __init__(self):
		super().__init__("dead_fire_coral_block", {})


class DeadHornCoralBlock(Block):
	def __init__(self):
		super().__init__("dead_horn_coral_block", {})


class DeadTubeCoralBlock(Block):
	def __init__(self):
		super().__init__("dead_tube_coral_block", {})


class DetectorRail(Block):
	def __init__(self):
		super().__init__("detector_rail", {})


class DiamondBlock(Block):
	def __init__(self):
		super().__init__("diamond_block", {})


class DiamondOre(Block):
	def __init__(self):
		super().__init__("diamond_ore", {})


class Diorite(Block):
	def __init__(self):
		super().__init__("diorite", {})


class DioriteSlab(Block):
	def __init__(self):
		super().__init__("diorite_slab", {})


class DioriteStairs(Block):
	def __init__(self):
		super().__init__("diorite_stairs", {})


class DioriteWall(Block):
	def __init__(self):
		super().__init__("diorite_wall", {})


class Dirt(Block):
	def __init__(self):
		super().__init__("dirt", {})


class Dispenser(Block):
	def __init__(self):
		super().__init__("dispenser", {})


class Dropper(Block):
	def __init__(self):
		super().__init__("dropper", {})


class DriedKelpBlock(Block):
	def __init__(self):
		super().__init__("dried_kelp_block", {})


class EmeraldBlock(Block):
	def __init__(self):
		super().__init__("emerald_block", {})


class EmeraldOre(Block):
	def __init__(self):
		super().__init__("emerald_ore", {})


class EnchantingTable(Block):
	def __init__(self):
		super().__init__("enchanting_table", {})


class EndPortalFrame(Block):
	def __init__(self):
		super().__init__("end_portal_frame", {})


class EndStone(Block):
	def __init__(self):
		super().__init__("end_stone", {})


class EndStoneBrickSlab(Block):
	def __init__(self):
		super().__init__("end_stone_brick_slab", {})


class EndStoneBrickStairs(Block):
	def __init__(self):
		super().__init__("end_stone_brick_stairs", {})


class EndStoneBrickWall(Block):
	def __init__(self):
		super().__init__("end_stone_brick_wall", {})


class EndStoneBricks(Block):
	def __init__(self):
		super().__init__("end_stone_bricks", {})


class EnderChest(Block):
	def __init__(self):
		super().__init__("ender_chest", {})


class Farmland(Block):
	def __init__(self):
		super().__init__("farmland", {})


class FireCoralBlock(Block):
	def __init__(self):
		super().__init__("fire_coral_block", {})


class FletchingTable(Block):
	def __init__(self):
		super().__init__("fletching_table", {})


class Furnace(Block):
	def __init__(self):
		super().__init__("furnace", {})


class GildedBlackstone(Block):
	def __init__(self):
		super().__init__("gilded_blackstone", {})


class Glass(Block):
	def __init__(self):
		super().__init__("glass", {})


class GlassPane(Block):
	def __init__(self):
		super().__init__("glass_pane", {})


class Glowstone(Block):
	def __init__(self):
		super().__init__("glowstone", {})


class GoldBlock(Block):
	def __init__(self):
		super().__init__("gold_block", {})


class GoldOre(Block):
	def __init__(self):
		super().__init__("gold_ore", {})


class Granite(Block):
	def __init__(self):
		super().__init__("granite", {})


class GraniteSlab(Block):
	def __init__(self):
		super().__init__("granite_slab", {})


class GraniteStairs(Block):
	def __init__(self):
		super().__init__("granite_stairs", {})


class GraniteWall(Block):
	def __init__(self):
		super().__init__("granite_wall", {})


class GrassBlock(Block):
	def __init__(self):
		super().__init__("grass_block", {})


class GrassPath(Block):
	def __init__(self):
		super().__init__("grass_path", {})


class Gravel(Block):
	def __init__(self):
		super().__init__("gravel", {})


class GrayConcrete(Block):
	def __init__(self):
		super().__init__("gray_concrete", {})


class GrayConcretePowder(Block):
	def __init__(self):
		super().__init__("gray_concrete_powder", {})


class GrayGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("gray_glazed_terracotta", {})


class GrayShulkerBox(Block):
	def __init__(self):
		super().__init__("gray_shulker_box", {})


class GrayStainedGlass(Block):
	def __init__(self):
		super().__init__("gray_stained_glass", {})


class GrayStainedGlassPane(Block):
	def __init__(self):
		super().__init__("gray_stained_glass_pane", {})


class GrayTerracotta(Block):
	def __init__(self):
		super().__init__("gray_terracotta", {})


class GrayWool(Block):
	def __init__(self):
		super().__init__("gray_wool", {})


class GreenConcrete(Block):
	def __init__(self):
		super().__init__("green_concrete", {})


class GreenConcretePowder(Block):
	def __init__(self):
		super().__init__("green_concrete_powder", {})


class GreenGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("green_glazed_terracotta", {})


class GreenShulkerBox(Block):
	def __init__(self):
		super().__init__("green_shulker_box", {})


class GreenStainedGlass(Block):
	def __init__(self):
		super().__init__("green_stained_glass", {})


class GreenStainedGlassPane(Block):
	def __init__(self):
		super().__init__("green_stained_glass_pane", {})


class GreenTerracotta(Block):
	def __init__(self):
		super().__init__("green_terracotta", {})


class GreenWool(Block):
	def __init__(self):
		super().__init__("green_wool", {})


class Grindstone(Block):
	def __init__(self):
		super().__init__("grindstone", {})


class HayBlock(Block):
	def __init__(self):
		super().__init__("hay_block", {})


class HeavyWeightedPressurePlate(Block):
	def __init__(self):
		super().__init__("heavy_weighted_pressure_plate", {})


class HoneyBlock(Block):
	def __init__(self):
		super().__init__("honey_block", {})


class HoneycombBlock(Block):
	def __init__(self):
		super().__init__("honeycomb_block", {})


class HornCoralBlock(Block):
	def __init__(self):
		super().__init__("horn_coral_block", {})


class Ice(Block):
	def __init__(self):
		super().__init__("ice", {})


class IronBars(Block):
	def __init__(self):
		super().__init__("iron_bars", {})


class IronBlock(Block):
	def __init__(self):
		super().__init__("iron_block", {})


class IronOre(Block):
	def __init__(self):
		super().__init__("iron_ore", {})


class IronTrapdoor(Block):
	def __init__(self):
		super().__init__("iron_trapdoor", {})


class JackOLantern(Block):
	def __init__(self):
		super().__init__("jack_o_lantern", {})


class Jukebox(Block):
	def __init__(self):
		super().__init__("jukebox", {})


class JungleButton(Block):
	def __init__(self):
		super().__init__("jungle_button", {})


class JungleDoor(Block):
	def __init__(self):
		super().__init__("jungle_door", {})


class JungleFence(Block):
	def __init__(self):
		super().__init__("jungle_fence", {})


class JungleFenceGate(Block):
	def __init__(self):
		super().__init__("jungle_fence_gate", {})


class JungleLeaves(Block):
	def __init__(self):
		super().__init__("jungle_leaves", {})


class JungleLog(Block):
	def __init__(self):
		super().__init__("jungle_log", {})


class JunglePlanks(Block):
	def __init__(self):
		super().__init__("jungle_planks", {})


class JunglePressurePlate(Block):
	def __init__(self):
		super().__init__("jungle_pressure_plate", {})


class JungleSlab(Block):
	def __init__(self):
		super().__init__("jungle_slab", {})


class JungleStairs(Block):
	def __init__(self):
		super().__init__("jungle_stairs", {})


class JungleTrapdoor(Block):
	def __init__(self):
		super().__init__("jungle_trapdoor", {})


class JungleWood(Block):
	def __init__(self):
		super().__init__("jungle_wood", {})


class Ladder(Block):
	def __init__(self):
		super().__init__("ladder", {})


class LapisBlock(Block):
	def __init__(self):
		super().__init__("lapis_block", {})


class LapisOre(Block):
	def __init__(self):
		super().__init__("lapis_ore", {})


class LightBlueConcrete(Block):
	def __init__(self):
		super().__init__("light_blue_concrete", {})


class LightBlueConcretePowder(Block):
	def __init__(self):
		super().__init__("light_blue_concrete_powder", {})


class LightBlueGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("light_blue_glazed_terracotta", {})


class LightBlueShulkerBox(Block):
	def __init__(self):
		super().__init__("light_blue_shulker_box", {})


class LightBlueStainedGlass(Block):
	def __init__(self):
		super().__init__("light_blue_stained_glass", {})


class LightBlueStainedGlassPane(Block):
	def __init__(self):
		super().__init__("light_blue_stained_glass_pane", {})


class LightBlueTerracotta(Block):
	def __init__(self):
		super().__init__("light_blue_terracotta", {})


class LightBlueWool(Block):
	def __init__(self):
		super().__init__("light_blue_wool", {})


class LightGrayConcrete(Block):
	def __init__(self):
		super().__init__("light_gray_concrete", {})


class LightGrayConcretePowder(Block):
	def __init__(self):
		super().__init__("light_gray_concrete_powder", {})


class LightGrayGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("light_gray_glazed_terracotta", {})


class LightGrayShulkerBox(Block):
	def __init__(self):
		super().__init__("light_gray_shulker_box", {})


class LightGrayStainedGlass(Block):
	def __init__(self):
		super().__init__("light_gray_stained_glass", {})


class LightGrayStainedGlassPane(Block):
	def __init__(self):
		super().__init__("light_gray_stained_glass_pane", {})


class LightGrayTerracotta(Block):
	def __init__(self):
		super().__init__("light_gray_terracotta", {})


class LightGrayWool(Block):
	def __init__(self):
		super().__init__("light_gray_wool", {})


class LightWeightedPressurePlate(Block):
	def __init__(self):
		super().__init__("light_weighted_pressure_plate", {})


class LimeConcrete(Block):
	def __init__(self):
		super().__init__("lime_concrete", {})


class LimeConcretePowder(Block):
	def __init__(self):
		super().__init__("lime_concrete_powder", {})


class LimeGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("lime_glazed_terracotta", {})


class LimeShulkerBox(Block):
	def __init__(self):
		super().__init__("lime_shulker_box", {})


class LimeStainedGlass(Block):
	def __init__(self):
		super().__init__("lime_stained_glass", {})


class LimeStainedGlassPane(Block):
	def __init__(self):
		super().__init__("lime_stained_glass_pane", {})


class LimeTerracotta(Block):
	def __init__(self):
		super().__init__("lime_terracotta", {})


class LimeWool(Block):
	def __init__(self):
		super().__init__("lime_wool", {})


class Lodestone(Block):
	def __init__(self):
		super().__init__("lodestone", {})


class Loom(Block):
	def __init__(self):
		super().__init__("loom", {})


class MagentaConcrete(Block):
	def __init__(self):
		super().__init__("magenta_concrete", {})


class MagentaConcretePowder(Block):
	def __init__(self):
		super().__init__("magenta_concrete_powder", {})


class MagentaGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("magenta_glazed_terracotta", {})


class MagentaShulkerBox(Block):
	def __init__(self):
		super().__init__("magenta_shulker_box", {})


class MagentaStainedGlass(Block):
	def __init__(self):
		super().__init__("magenta_stained_glass", {})


class MagentaStainedGlassPane(Block):
	def __init__(self):
		super().__init__("magenta_stained_glass_pane", {})


class MagentaTerracotta(Block):
	def __init__(self):
		super().__init__("magenta_terracotta", {})


class MagentaWool(Block):
	def __init__(self):
		super().__init__("magenta_wool", {})


class MagmaBlock(Block):
	def __init__(self):
		super().__init__("magma_block", {})


class Melon(Block):
	def __init__(self):
		super().__init__("melon", {})


class MossyCobblestone(Block):
	def __init__(self):
		super().__init__("mossy_cobblestone", {})


class MossyCobblestoneSlab(Block):
	def __init__(self):
		super().__init__("mossy_cobblestone_slab", {})


class MossyCobblestoneStairs(Block):
	def __init__(self):
		super().__init__("mossy_cobblestone_stairs", {})


class MossyCobblestoneWall(Block):
	def __init__(self):
		super().__init__("mossy_cobblestone_wall", {})


class MossyStoneBrickSlab(Block):
	def __init__(self):
		super().__init__("mossy_stone_brick_slab", {})


class MossyStoneBrickStairs(Block):
	def __init__(self):
		super().__init__("mossy_stone_brick_stairs", {})


class MossyStoneBrickWall(Block):
	def __init__(self):
		super().__init__("mossy_stone_brick_wall", {})


class MossyStoneBricks(Block):
	def __init__(self):
		super().__init__("mossy_stone_bricks", {})


class MushroomStem(Block):
	def __init__(self):
		super().__init__("mushroom_stem", {})


class Mycelium(Block):
	def __init__(self):
		super().__init__("mycelium", {})


class NetherBrickFence(Block):
	def __init__(self):
		super().__init__("nether_brick_fence", {})


class NetherBrickSlab(Block):
	def __init__(self):
		super().__init__("nether_brick_slab", {})


class NetherBrickStairs(Block):
	def __init__(self):
		super().__init__("nether_brick_stairs", {})


class NetherBrickWall(Block):
	def __init__(self):
		super().__init__("nether_brick_wall", {})


class NetherBricks(Block):
	def __init__(self):
		super().__init__("nether_bricks", {})


class NetherGoldOre(Block):
	def __init__(self):
		super().__init__("nether_gold_ore", {})


class NetherQuartzOre(Block):
	def __init__(self):
		super().__init__("nether_quartz_ore", {})


class NetherWartBlock(Block):
	def __init__(self):
		super().__init__("nether_wart_block", {})


class NetheriteBlock(Block):
	def __init__(self):
		super().__init__("netherite_block", {})


class Netherrack(Block):
	def __init__(self):
		super().__init__("netherrack", {})


class NoteBlock(Block):
	def __init__(self):
		super().__init__("note_block", {})


class OakButton(Block):
	def __init__(self):
		super().__init__("oak_button", {})


class OakFence(Block):
	def __init__(self):
		super().__init__("oak_fence", {})


class OakFenceGate(Block):
	def __init__(self):
		super().__init__("oak_fence_gate", {})


class OakLeaves(Block):
	def __init__(self):
		super().__init__("oak_leaves", {})


class OakLog(Block):
	def __init__(self):
		super().__init__("oak_log", {})


class OakPlanks(Block):
	def __init__(self):
		super().__init__("oak_planks", {})


class OakPressurePlate(Block):
	def __init__(self):
		super().__init__("oak_pressure_plate", {})


class OakSlab(Block):
	def __init__(self):
		super().__init__("oak_slab", {})


class OakStairs(Block):
	def __init__(self):
		super().__init__("oak_stairs", {})


class OakTrapdoor(Block):
	def __init__(self):
		super().__init__("oak_trapdoor", {})


class OakWood(Block):
	def __init__(self):
		super().__init__("oak_wood", {})


class Observer(Block):
	def __init__(self):
		super().__init__("observer", {})


class Obsidian(Block):
	def __init__(self):
		super().__init__("obsidian", {})


class OrangeConcrete(Block):
	def __init__(self):
		super().__init__("orange_concrete", {})


class OrangeConcretePowder(Block):
	def __init__(self):
		super().__init__("orange_concrete_powder", {})


class OrangeGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("orange_glazed_terracotta", {})


class OrangeShulkerBox(Block):
	def __init__(self):
		super().__init__("orange_shulker_box", {})


class OrangeStainedGlass(Block):
	def __init__(self):
		super().__init__("orange_stained_glass", {})


class OrangeStainedGlassPane(Block):
	def __init__(self):
		super().__init__("orange_stained_glass_pane", {})


class OrangeTerracotta(Block):
	def __init__(self):
		super().__init__("orange_terracotta", {})


class OrangeWool(Block):
	def __init__(self):
		super().__init__("orange_wool", {})


class PackedIce(Block):
	def __init__(self):
		super().__init__("packed_ice", {})


class PetrifiedOakSlab(Block):
	def __init__(self):
		super().__init__("petrified_oak_slab", {})


class PinkConcrete(Block):
	def __init__(self):
		super().__init__("pink_concrete", {})


class PinkConcretePowder(Block):
	def __init__(self):
		super().__init__("pink_concrete_powder", {})


class PinkGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("pink_glazed_terracotta", {})


class PinkShulkerBox(Block):
	def __init__(self):
		super().__init__("pink_shulker_box", {})


class PinkStainedGlass(Block):
	def __init__(self):
		super().__init__("pink_stained_glass", {})


class PinkStainedGlassPane(Block):
	def __init__(self):
		super().__init__("pink_stained_glass_pane", {})


class PinkTerracotta(Block):
	def __init__(self):
		super().__init__("pink_terracotta", {})


class PinkWool(Block):
	def __init__(self):
		super().__init__("pink_wool", {})


class Piston(Block):
	def __init__(self):
		super().__init__("piston", {})


class Podzol(Block):
	def __init__(self):
		super().__init__("podzol", {})


class PolishedAndesite(Block):
	def __init__(self):
		super().__init__("polished_andesite", {})


class PolishedAndesiteSlab(Block):
	def __init__(self):
		super().__init__("polished_andesite_slab", {})


class PolishedAndesiteStairs(Block):
	def __init__(self):
		super().__init__("polished_andesite_stairs", {})


class PolishedBasalt(Block):
	def __init__(self):
		super().__init__("polished_basalt", {})


class PolishedBlackstone(Block):
	def __init__(self):
		super().__init__("polished_blackstone", {})


class PolishedBlackstoneBrickSlab(Block):
	def __init__(self):
		super().__init__("polished_blackstone_brick_slab", {})


class PolishedBlackstoneBrickStairs(Block):
	def __init__(self):
		super().__init__("polished_blackstone_brick_stairs", {})


class PolishedBlackstoneBrickWall(Block):
	def __init__(self):
		super().__init__("polished_blackstone_brick_wall", {})


class PolishedBlackstoneBricks(Block):
	def __init__(self):
		super().__init__("polished_blackstone_bricks", {})


class PolishedBlackstoneButton(Block):
	def __init__(self):
		super().__init__("polished_blackstone_button", {})


class PolishedBlackstonePressurePlate(Block):
	def __init__(self):
		super().__init__("polished_blackstone_pressure_plate", {})


class PolishedBlackstoneSlab(Block):
	def __init__(self):
		super().__init__("polished_blackstone_slab", {})


class PolishedBlackstoneStairs(Block):
	def __init__(self):
		super().__init__("polished_blackstone_stairs", {})


class PolishedBlackstoneWall(Block):
	def __init__(self):
		super().__init__("polished_blackstone_wall", {})


class PolishedDiorite(Block):
	def __init__(self):
		super().__init__("polished_diorite", {})


class PolishedDioriteSlab(Block):
	def __init__(self):
		super().__init__("polished_diorite_slab", {})


class PolishedDioriteStairs(Block):
	def __init__(self):
		super().__init__("polished_diorite_stairs", {})


class PolishedGranite(Block):
	def __init__(self):
		super().__init__("polished_granite", {})


class PolishedGraniteSlab(Block):
	def __init__(self):
		super().__init__("polished_granite_slab", {})


class PolishedGraniteStairs(Block):
	def __init__(self):
		super().__init__("polished_granite_stairs", {})


class Prismarine(Block):
	def __init__(self):
		super().__init__("prismarine", {})


class PrismarineBrickSlab(Block):
	def __init__(self):
		super().__init__("prismarine_brick_slab", {})


class PrismarineBrickStairs(Block):
	def __init__(self):
		super().__init__("prismarine_brick_stairs", {})


class PrismarineBricks(Block):
	def __init__(self):
		super().__init__("prismarine_bricks", {})


class PrismarineSlab(Block):
	def __init__(self):
		super().__init__("prismarine_slab", {})


class PrismarineStairs(Block):
	def __init__(self):
		super().__init__("prismarine_stairs", {})


class PrismarineWall(Block):
	def __init__(self):
		super().__init__("prismarine_wall", {})


class Pumpkin(Block):
	def __init__(self):
		super().__init__("pumpkin", {})


class PurpleConcrete(Block):
	def __init__(self):
		super().__init__("purple_concrete", {})


class PurpleConcretePowder(Block):
	def __init__(self):
		super().__init__("purple_concrete_powder", {})


class PurpleGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("purple_glazed_terracotta", {})


class PurpleShulkerBox(Block):
	def __init__(self):
		super().__init__("purple_shulker_box", {})


class PurpleStainedGlass(Block):
	def __init__(self):
		super().__init__("purple_stained_glass", {})


class PurpleStainedGlassPane(Block):
	def __init__(self):
		super().__init__("purple_stained_glass_pane", {})


class PurpleTerracotta(Block):
	def __init__(self):
		super().__init__("purple_terracotta", {})


class PurpleWool(Block):
	def __init__(self):
		super().__init__("purple_wool", {})


class PurpurBlock(Block):
	def __init__(self):
		super().__init__("purpur_block", {})


class PurpurPillar(Block):
	def __init__(self):
		super().__init__("purpur_pillar", {})


class PurpurSlab(Block):
	def __init__(self):
		super().__init__("purpur_slab", {})


class PurpurStairs(Block):
	def __init__(self):
		super().__init__("purpur_stairs", {})


class QuartzBlock(Block):
	def __init__(self):
		super().__init__("quartz_block", {})


class QuartzBricks(Block):
	def __init__(self):
		super().__init__("quartz_bricks", {})


class QuartzPillar(Block):
	def __init__(self):
		super().__init__("quartz_pillar", {})


class QuartzSlab(Block):
	def __init__(self):
		super().__init__("quartz_slab", {})


class QuartzStairs(Block):
	def __init__(self):
		super().__init__("quartz_stairs", {})


class Rail(Block):
	def __init__(self):
		super().__init__("rail", {})


class RedConcrete(Block):
	def __init__(self):
		super().__init__("red_concrete", {})


class RedConcretePowder(Block):
	def __init__(self):
		super().__init__("red_concrete_powder", {})


class RedGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("red_glazed_terracotta", {})


class RedMushroomBlock(Block):
	def __init__(self):
		super().__init__("red_mushroom_block", {})


class RedNetherBrickSlab(Block):
	def __init__(self):
		super().__init__("red_nether_brick_slab", {})


class RedNetherBrickStairs(Block):
	def __init__(self):
		super().__init__("red_nether_brick_stairs", {})


class RedNetherBrickWall(Block):
	def __init__(self):
		super().__init__("red_nether_brick_wall", {})


class RedNetherBricks(Block):
	def __init__(self):
		super().__init__("red_nether_bricks", {})


class RedSand(Block):
	def __init__(self):
		super().__init__("red_sand", {})


class RedSandstone(Block):
	def __init__(self):
		super().__init__("red_sandstone", {})


class RedSandstoneSlab(Block):
	def __init__(self):
		super().__init__("red_sandstone_slab", {})


class RedSandstoneStairs(Block):
	def __init__(self):
		super().__init__("red_sandstone_stairs", {})


class RedSandstoneWall(Block):
	def __init__(self):
		super().__init__("red_sandstone_wall", {})


class RedShulkerBox(Block):
	def __init__(self):
		super().__init__("red_shulker_box", {})


class RedStainedGlass(Block):
	def __init__(self):
		super().__init__("red_stained_glass", {})


class RedStainedGlassPane(Block):
	def __init__(self):
		super().__init__("red_stained_glass_pane", {})


class RedTerracotta(Block):
	def __init__(self):
		super().__init__("red_terracotta", {})


class RedWool(Block):
	def __init__(self):
		super().__init__("red_wool", {})


class RedstoneBlock(Block):
	def __init__(self):
		super().__init__("redstone_block", {})


class RedstoneLamp(Block):
	def __init__(self):
		super().__init__("redstone_lamp", {})


class RedstoneOre(Block):
	def __init__(self):
		super().__init__("redstone_ore", {})


class RedstoneTorch(Block):
	def __init__(self):
		super().__init__("redstone_torch", {})


class Repeater(Block):
	def __init__(self):
		super().__init__("repeater", {})


class RepeatingCommandBlock(Block):
	def __init__(self):
		super().__init__("repeating_command_block", {})


class RespawnAnchor(Block):
	def __init__(self):
		super().__init__("respawn_anchor", {})


class Sand(Block):
	def __init__(self):
		super().__init__("sand", {})


class Sandstone(Block):
	def __init__(self):
		super().__init__("sandstone", {})


class SandstoneSlab(Block):
	def __init__(self):
		super().__init__("sandstone_slab", {})


class SandstoneStairs(Block):
	def __init__(self):
		super().__init__("sandstone_stairs", {})


class SandstoneWall(Block):
	def __init__(self):
		super().__init__("sandstone_wall", {})


class SeaLantern(Block):
	def __init__(self):
		super().__init__("sea_lantern", {})


class Shroomlight(Block):
	def __init__(self):
		super().__init__("shroomlight", {})


class ShulkerBox(Block):
	def __init__(self):
		super().__init__("shulker_box", {})


class SlimeBlock(Block):
	def __init__(self):
		super().__init__("slime_block", {})


class SmithingTable(Block):
	def __init__(self):
		super().__init__("smithing_table", {})


class Smoker(Block):
	def __init__(self):
		super().__init__("smoker", {})


class SmoothQuartz(Block):
	def __init__(self):
		super().__init__("smooth_quartz", {})


class SmoothQuartzSlab(Block):
	def __init__(self):
		super().__init__("smooth_quartz_slab", {})


class SmoothQuartzStairs(Block):
	def __init__(self):
		super().__init__("smooth_quartz_stairs", {})


class SmoothRedSandstone(Block):
	def __init__(self):
		super().__init__("smooth_red_sandstone", {})


class SmoothRedSandstoneSlab(Block):
	def __init__(self):
		super().__init__("smooth_red_sandstone_slab", {})


class SmoothRedSandstoneStairs(Block):
	def __init__(self):
		super().__init__("smooth_red_sandstone_stairs", {})


class SmoothSandstone(Block):
	def __init__(self):
		super().__init__("smooth_sandstone", {})


class SmoothSandstoneSlab(Block):
	def __init__(self):
		super().__init__("smooth_sandstone_slab", {})


class SmoothSandstoneStairs(Block):
	def __init__(self):
		super().__init__("smooth_sandstone_stairs", {})


class SmoothStone(Block):
	def __init__(self):
		super().__init__("smooth_stone", {})


class SmoothStoneSlab(Block):
	def __init__(self):
		super().__init__("smooth_stone_slab", {})


class Snow(Block):
	def __init__(self):
		super().__init__("snow", {})


class SnowBlock(Block):
	def __init__(self):
		super().__init__("snow_block", {})


class SoulSand(Block):
	def __init__(self):
		super().__init__("soul_sand", {})


class SoulSoil(Block):
	def __init__(self):
		super().__init__("soul_soil", {})


class SoulTorch(Block):
	def __init__(self):
		super().__init__("soul_torch", {})


class Sponge(Block):
	def __init__(self):
		super().__init__("sponge", {})


class SpruceButton(Block):
	def __init__(self):
		super().__init__("spruce_button", {})


class SpruceFence(Block):
	def __init__(self):
		super().__init__("spruce_fence", {})


class SpruceFenceGate(Block):
	def __init__(self):
		super().__init__("spruce_fence_gate", {})


class SpruceLeaves(Block):
	def __init__(self):
		super().__init__("spruce_leaves", {})


class SpruceLog(Block):
	def __init__(self):
		super().__init__("spruce_log", {})


class SprucePlanks(Block):
	def __init__(self):
		super().__init__("spruce_planks", {})


class SprucePressurePlate(Block):
	def __init__(self):
		super().__init__("spruce_pressure_plate", {})


class SpruceSlab(Block):
	def __init__(self):
		super().__init__("spruce_slab", {})


class SpruceStairs(Block):
	def __init__(self):
		super().__init__("spruce_stairs", {})


class SpruceTrapdoor(Block):
	def __init__(self):
		super().__init__("spruce_trapdoor", {})


class SpruceWood(Block):
	def __init__(self):
		super().__init__("spruce_wood", {})


class StickyPiston(Block):
	def __init__(self):
		super().__init__("sticky_piston", {})


class Stone(Block):
	def __init__(self):
		super().__init__("stone", {})


class StoneBrickSlab(Block):
	def __init__(self):
		super().__init__("stone_brick_slab", {})


class StoneBrickStairs(Block):
	def __init__(self):
		super().__init__("stone_brick_stairs", {})


class StoneBrickWall(Block):
	def __init__(self):
		super().__init__("stone_brick_wall", {})


class StoneBricks(Block):
	def __init__(self):
		super().__init__("stone_bricks", {})


class StoneButton(Block):
	def __init__(self):
		super().__init__("stone_button", {})


class StonePressurePlate(Block):
	def __init__(self):
		super().__init__("stone_pressure_plate", {})


class StoneSlab(Block):
	def __init__(self):
		super().__init__("stone_slab", {})


class StoneStairs(Block):
	def __init__(self):
		super().__init__("stone_stairs", {})


class Stonecutter(Block):
	def __init__(self):
		super().__init__("stonecutter", {})


class StrippedAcaciaLog(Block):
	def __init__(self):
		super().__init__("stripped_acacia_log", {})


class StrippedAcaciaWood(Block):
	def __init__(self):
		super().__init__("stripped_acacia_wood", {})


class StrippedBirchLog(Block):
	def __init__(self):
		super().__init__("stripped_birch_log", {})


class StrippedBirchWood(Block):
	def __init__(self):
		super().__init__("stripped_birch_wood", {})


class StrippedCrimsonHyphae(Block):
	def __init__(self):
		super().__init__("stripped_crimson_hyphae", {})


class StrippedCrimsonStem(Block):
	def __init__(self):
		super().__init__("stripped_crimson_stem", {})


class StrippedDarkOakLog(Block):
	def __init__(self):
		super().__init__("stripped_dark_oak_log", {})


class StrippedDarkOakWood(Block):
	def __init__(self):
		super().__init__("stripped_dark_oak_wood", {})


class StrippedJungleLog(Block):
	def __init__(self):
		super().__init__("stripped_jungle_log", {})


class StrippedJungleWood(Block):
	def __init__(self):
		super().__init__("stripped_jungle_wood", {})


class StrippedOakLog(Block):
	def __init__(self):
		super().__init__("stripped_oak_log", {})


class StrippedOakWood(Block):
	def __init__(self):
		super().__init__("stripped_oak_wood", {})


class StrippedSpruceLog(Block):
	def __init__(self):
		super().__init__("stripped_spruce_log", {})


class StrippedSpruceWood(Block):
	def __init__(self):
		super().__init__("stripped_spruce_wood", {})


class StrippedWarpedHyphae(Block):
	def __init__(self):
		super().__init__("stripped_warped_hyphae", {})


class StrippedWarpedStem(Block):
	def __init__(self):
		super().__init__("stripped_warped_stem", {})


class Target(Block):
	def __init__(self):
		super().__init__("target", {})


class Terracotta(Block):
	def __init__(self):
		super().__init__("terracotta", {})


class Tnt(Block):
	def __init__(self):
		super().__init__("tnt", {})


class Torch(Block):
	def __init__(self):
		super().__init__("torch", {})


class TrappedChest(Block):
	def __init__(self):
		super().__init__("trapped_chest", {})


class TubeCoralBlock(Block):
	def __init__(self):
		super().__init__("tube_coral_block", {})


class WarpedFence(Block):
	def __init__(self):
		super().__init__("warped_fence", {})


class WarpedFenceGate(Block):
	def __init__(self):
		super().__init__("warped_fence_gate", {})


class WarpedButton(Block):
	def __init__(self):
		super().__init__("warped_button", {})


class WarpedHyphae(Block):
	def __init__(self):
		super().__init__("warped_hyphae", {})


class WarpedNylium(Block):
	def __init__(self):
		super().__init__("warped_nylium", {})


class WarpedPlanks(Block):
	def __init__(self):
		super().__init__("warped_planks", {})


class WarpedPressurePlate(Block):
	def __init__(self):
		super().__init__("warped_pressure_plate", {})


class WarpedSlab(Block):
	def __init__(self):
		super().__init__("warped_slab", {})


class WarpedStairs(Block):
	def __init__(self):
		super().__init__("warped_stairs", {})


class WarpedStem(Block):
	def __init__(self):
		super().__init__("warped_stem", {})


class WarpedTrapdoor(Block):
	def __init__(self):
		super().__init__("warped_trapdoor", {})


class WarpedWartBlock(Block):
	def __init__(self):
		super().__init__("warped_wart_block", {})


class Water(Block):
	def __init__(self):
		super().__init__("water", {})


class WetSponge(Block):
	def __init__(self):
		super().__init__("wet_sponge", {})


class WhiteConcrete(Block):
	def __init__(self):
		super().__init__("white_concrete", {})


class WhiteConcretePowder(Block):
	def __init__(self):
		super().__init__("white_concrete_powder", {})


class WhiteGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("white_glazed_terracotta", {})


class WhiteShulkerBox(Block):
	def __init__(self):
		super().__init__("white_shulker_box", {})


class WhiteStainedGlass(Block):
	def __init__(self):
		super().__init__("white_stained_glass", {})


class WhiteStainedGlassPane(Block):
	def __init__(self):
		super().__init__("white_stained_glass_pane", {})


class WhiteTerracotta(Block):
	def __init__(self):
		super().__init__("white_terracotta", {})


class WhiteWool(Block):
	def __init__(self):
		super().__init__("white_wool", {})


class YellowConcrete(Block):
	def __init__(self):
		super().__init__("yellow_concrete", {})


class YellowConcretePowder(Block):
	def __init__(self):
		super().__init__("yellow_concrete_powder", {})


class YellowGlazedTerracotta(Block):
	def __init__(self):
		super().__init__("yellow_glazed_terracotta", {})


class YellowShulkerBox(Block):
	def __init__(self):
		super().__init__("yellow_shulker_box", {})


class YellowStainedGlass(Block):
	def __init__(self):
		super().__init__("yellow_stained_glass", {})


class YellowStainedGlassPane(Block):
	def __init__(self):
		super().__init__("yellow_stained_glass_pane", {})


class YellowTerracotta(Block):
	def __init__(self):
		super().__init__("yellow_terracotta", {})


class YellowWool(Block):
	def __init__(self):
		super().__init__("yellow_wool", {})


class BlockList:
	def __init__(self):
		pass

	ACACIA_BUTTON = AcaciaButton()
	ACACIA_DOOR = AcaciaDoor()
	ACACIA_FENCE = AcaciaFence()
	ACACIA_FENCE_GATE = AcaciaFenceGate()
	ACACIA_LEAVES = AcaciaLeaves()
	ACACIA_LOG = AcaciaLog()
	ACACIA_PLANKS = AcaciaPlanks()
	ACACIA_PRESSURE_PLATE = AcaciaPressurePlate()
	ACACIA_SIGN = AcaciaSign()
	ACACIA_SLAB = AcaciaSlab()
	ACACIA_STAIRS = AcaciaStairs()
	ACACIA_TRAPDOOR = AcaciaTrapdoor()
	ACACIA_WOOD = AcaciaWood()
	ACTIVATOR_RAIL = ActivatorRail()
	AIR = Air()
	ANCIENT_DEBRIS = AncientDebris()
	ANDESITE = Andesite()
	ANDESITE_SLAB = AndesiteSlab()
	ANDESITE_STAIRS = AndesiteStairs()
	ANDESITE_WALL = AndesiteWall()
	ANVIL = Anvil()
	BARREL = Barrel()
	BASALT = Basalt()
	BARRIER = Barrier()
	BEACON = Beacon()
	BEDROCK = Bedrock()
	BEE_NEST = BeeNest()
	BEEHIVE = Beehive()
	BELL = Bell()
	BIRCH_BUTTON = BirchButton()
	BIRCH_DOOR = BirchDoor()
	BIRCH_FENCE = BirchFence()
	BIRCH_FENCE_GATE = BirchFenceGate()
	BIRCH_LEAVES = BirchLeaves()
	BIRCH_LOG = BirchLog()
	BIRCH_PLANKS = BirchPlanks()
	BIRCH_PRESSURE_PLATE = BirchPressurePlate()
	BIRCH_SIGN = BirchSign()
	BIRCH_SLAB = BirchSlab()
	BIRCH_STAIRS = BirchStairs()
	BIRCH_TRAPDOOR = BirchTrapdoor()
	BIRCH_WOOD = BirchWood()
	BLACK_CONCRETE = BlackConcrete()
	BLACK_CONCRETE_POWDER = BlackConcretePowder()
	BLACK_GLAZED_TERRACOTTA = BlackGlazedTerracotta()
	BLACK_SHULKER_BOX = BlackShulkerBox()
	BLACK_STAINED_GLASS = BlackStainedGlass()
	BLACK_STAINED_GLASS_PANE = BlackStainedGlassPane()
	BLACK_TERRACOTTA = BlackTerracotta()
	BLACK_WOOL = BlackWool()
	BLACKSTONE = Blackstone()
	BLACKSTONE_SLAB = BlackstoneSlab()
	BLACKSTONE_STAIRS = BlackstoneStairs()
	BLACKSTONE_WALL = BlackstoneWall()
	BLAST_FURNACE = BlastFurnace()
	BLUE_CONCRETE = BlueConcrete()
	BLUE_CONCRETE_POWDER = BlueConcretePowder()
	BLUE_GLAZED_TERRACOTTA = BlueGlazedTerracotta()
	BLUE_ICE = BlueIce()
	BLUE_SHULKER_BOX = BlueShulkerBox()
	BLUE_STAINED_GLASS = BlueStainedGlass()
	BLUE_STAINED_GLASS_PANE = BlueStainedGlassPane()
	BLUE_TERRACOTTA = BlueTerracotta()
	BLUE_WOOL = BlueWool()
	BONE_BLOCK = BoneBlock()
	BOOKSHELF = Bookshelf()
	BRAIN_CORAL_BLOCK = BrainCoralBlock()
	BRICK_SLAB = BrickSlab()
	BRICK_STAIRS = BrickStairs()
	BRICK_WALL = BrickWall()
	BRICKS = Bricks()
	BROWN_CONCRETE = BrownConcrete()
	BROWN_CONCRETE_POWDER = BrownConcretePowder()
	BROWN_GLAZED_TERRACOTTA = BrownGlazedTerracotta()
	BROWN_MUSHROOM_BLOCK = BrownMushroomBlock()
	BROWN_SHULKER_BOX = BrownShulkerBox()
	BROWN_STAINED_GLASS = BrownStainedGlass()
	BROWN_STAINED_GLASS_PANE = BrownStainedGlassPane()
	BROWN_TERRACOTTA = BrownTerracotta()
	BROWN_WOOL = BrownWool()
	BUBBLE_CORAL_BLOCK = BubbleCoralBlock()
	CACTUS = Cactus()
	CARTOGRAPHY_TABLE = CartographyTable()
	CARVED_PUMPKIN = CarvedPumpkin()
	CAULDRON = Cauldron()
	CHAIN = Chain()
	CHAIN_COMMAND_BLOCK = ChainCommandBlock()
	CHEST = Chest()
	CHIPPED_ANVIL = ChippedAnvil()
	CHISELED_NETHER_BRICKS = ChiseledNetherBricks()
	CHISELED_POLISHED_BLACKSTONE = ChiseledPolishedBlackstone()
	CHISELED_QUARTZ_BLOCK = ChiseledQuartzBlock()
	CHISELED_RED_SANDSTONE = ChiseledRedSandstone()
	CHISELED_SANDSTONE = ChiseledSandstone()
	CHISELED_STONE_BRICKS = ChiseledStoneBricks()
	CHORUS_FLOWER = ChorusFlower()
	CHORUS_PLANT = ChorusPlant()
	CLAY = Clay()
	COAL_BLOCK = CoalBlock()
	COAL_ORE = CoalOre()
	COARSE_DIRT = CoarseDirt()
	COBBLESTONE = Cobblestone()
	COBBLESTONE_SLAB = CobblestoneSlab()
	COBBLESTONE_STAIRS = CobblestoneStairs()
	COBBLESTONE_WALL = CobblestoneWall()
	COBWEB = Cobweb()
	COMMAND_BLOCK = CommandBlock()
	COMPARATOR = Comparator()
	COMPOSTER = Composter()
	CONDUIT = Conduit()
	CRACKED_NETHER_BRICKS = CrackedNetherBricks()
	CRACKED_POLISHED_BLACKSTONE_BRICKS = CrackedPolishedBlackstoneBricks()
	CRACKED_STONE_BRICKS = CrackedStoneBricks()
	CRAFTING_TABLE = CraftingTable()
	CRIMSON_BUTTON = CrimsonButton()
	CRIMSON_DOOR = CrimsonDoor()
	CRIMSON_FENCE = CrimsonFence()
	CRIMSON_FENCE_GATE = CrimsonFenceGate()
	CRIMSON_HYPHAE = CrimsonHyphae()
	CRIMSON_NYLIUM = CrimsonNylium()
	CRIMSON_PLANKS = CrimsonPlanks()
	CRIMSON_PRESSURE_PLATE = CrimsonPressurePlate()
	CRIMSON_SIGN = CrimsonSign()
	CRIMSON_SLAB = CrimsonSlab()
	CRIMSON_STAIRS = CrimsonStairs()
	CRIMSON_STEM = CrimsonStem()
	CRIMSON_TRAPDOOR = CrimsonTrapdoor()
	CRYING_OBSIDIAN = CryingObsidian()
	CUT_RED_SANDSTONE = CutRedSandstone()
	CUT_RED_SANDSTONE_SLAB = CutRedSandstoneSlab()
	CUT_SANDSTONE = CutSandstone()
	CUT_SANDSTONE_SLAB = CutSandstoneSlab()
	CYAN_CONCRETE = CyanConcrete()
	CYAN_CONCRETE_POWDER = CyanConcretePowder()
	CYAN_GLAZED_TERRACOTTA = CyanGlazedTerracotta()
	CYAN_SHULKER_BOX = CyanShulkerBox()
	CYAN_STAINED_GLASS = CyanStainedGlass()
	CYAN_STAINED_GLASS_PANE = CyanStainedGlassPane()
	CYAN_TERRACOTTA = CyanTerracotta()
	CYAN_WOOL = CyanWool()
	DAMAGED_ANVIL = DamagedAnvil()
	DARK_OAK_BUTTON = DarkOakButton()
	DARK_OAK_FENCE = DarkOakFence()
	DARK_OAK_FENCE_GATE = DarkOakFenceGate()
	DARK_OAK_LEAVES = DarkOakLeaves()
	DARK_OAK_LOG = DarkOakLog()
	DARK_OAK_PLANKS = DarkOakPlanks()
	DARK_OAK_PRESSURE_PLATE = DarkOakPressurePlate()
	DARK_OAK_SIGN = DarkOakSign()
	DARK_OAK_SLAB = DarkOakSlab()
	DARK_OAK_STAIRS = DarkOakStairs()
	DARK_OAK_TRAPDOOR = DarkOakTrapdoor()
	DARK_OAK_WOOD = DarkOakWood()
	DARK_PRISMARINE = DarkPrismarine()
	DARK_PRISMARINE_SLAB = DarkPrismarineSlab()
	DARK_PRISMARINE_STAIRS = DarkPrismarineStairs()
	DAYLIGHT_DETECTOR = DaylightDetector()
	DEAD_BRAIN_CORAL_BLOCK = DeadBrainCoralBlock()
	DEAD_BUBBLE_CORAL_BLOCK = DeadBubbleCoralBlock()
	DEAD_FIRE_CORAL_BLOCK = DeadFireCoralBlock()
	DEAD_HORN_CORAL_BLOCK = DeadHornCoralBlock()
	DEAD_TUBE_CORAL_BLOCK = DeadTubeCoralBlock()
	DETECTOR_RAIL = DetectorRail()
	DIAMOND_BLOCK = DiamondBlock()
	DIAMOND_ORE = DiamondOre()
	DIORITE = Diorite()
	DIORITE_SLAB = DioriteSlab()
	DIORITE_STAIRS = DioriteStairs()
	DIORITE_WALL = DioriteWall()
	DIRT = Dirt()
	DISPENSER = Dispenser()
	DROPPER = Dropper()
	DRIED_KELP_BLOCK = DriedKelpBlock()
	EMERALD_BLOCK = EmeraldBlock()
	EMERALD_ORE = EmeraldOre()
	ENCHANTING_TABLE = EnchantingTable()
	END_PORTAL_FRAME = EndPortalFrame()
	END_STONE = EndStone()
	END_STONE_BRICK_SLAB = EndStoneBrickSlab()
	END_STONE_BRICK_STAIRS = EndStoneBrickStairs()
	END_STONE_BRICK_WALL = EndStoneBrickWall()
	END_STONE_BRICKS = EndStoneBricks()
	ENDER_CHEST = EnderChest()
	FARMLAND = Farmland()
	FIRE_CORAL_BLOCK = FireCoralBlock()
	FLETCHING_TABLE = FletchingTable()
	FURNACE = Furnace()
	GILDED_BLACKSTONE = GildedBlackstone()
	GLASS = Glass()
	GLASS_PANE = GlassPane()
	GLOWSTONE = Glowstone()
	GOLD_BLOCK = GoldBlock()
	GOLD_ORE = GoldOre()
	GRANITE = Granite()
	GRANITE_SLAB = GraniteSlab()
	GRANITE_STAIRS = GraniteStairs()
	GRANITE_WALL = GraniteWall()
	GRASS_BLOCK = GrassBlock()
	GRASS_PATH = GrassPath()
	GRAVEL = Gravel()
	GRAY_CONCRETE = GrayConcrete()
	GRAY_CONCRETE_POWDER = GrayConcretePowder()
	GRAY_GLAZED_TERRACOTTA = GrayGlazedTerracotta()
	GRAY_SHULKER_BOX = GrayShulkerBox()
	GRAY_STAINED_GLASS = GrayStainedGlass()
	GRAY_STAINED_GLASS_PANE = GrayStainedGlassPane()
	GRAY_TERRACOTTA = GrayTerracotta()
	GRAY_WOOL = GrayWool()
	GREEN_CONCRETE = GreenConcrete()
	GREEN_CONCRETE_POWDER = GreenConcretePowder()
	GREEN_GLAZED_TERRACOTTA = GreenGlazedTerracotta()
	GREEN_SHULKER_BOX = GreenShulkerBox()
	GREEN_STAINED_GLASS = GreenStainedGlass()
	GREEN_STAINED_GLASS_PANE = GreenStainedGlassPane()
	GREEN_TERRACOTTA = GreenTerracotta()
	GREEN_WOOL = GreenWool()
	GRINDSTONE = Grindstone()
	HAY_BLOCK = HayBlock()
	HEAVY_WEIGHTED_PRESSURE_PLATE = HeavyWeightedPressurePlate()
	HONEY_BLOCK = HoneyBlock()
	HONEYCOMB_BLOCK = HoneycombBlock()
	HORN_CORAL_BLOCK = HornCoralBlock()
	ICE = Ice()
	IRON_BARS = IronBars()
	IRON_BLOCK = IronBlock()
	IRON_ORE = IronOre()
	IRON_TRAPDOOR = IronTrapdoor()
	JACK_O_LANTERN = JackOLantern()
	JUKEBOX = Jukebox()
	JUNGLE_BUTTON = JungleButton()
	JUNGLE_DOOR = JungleDoor()
	JUNGLE_FENCE = JungleFence()
	JUNGLE_FENCE_GATE = JungleFenceGate()
	JUNGLE_LEAVES = JungleLeaves()
	JUNGLE_LOG = JungleLog()
	JUNGLE_PLANKS = JunglePlanks()
	JUNGLE_PRESSURE_PLATE = JunglePressurePlate()
	JUNGLE_SLAB = JungleSlab()
	JUNGLE_STAIRS = JungleStairs()
	JUNGLE_TRAPDOOR = JungleTrapdoor()
	JUNGLE_WOOD = JungleWood()
	LADDER = Ladder()
	LAPIS_BLOCK = LapisBlock()
	LAPIS_ORE = LapisOre()
	LIGHT_BLUE_CONCRETE = LightBlueConcrete()
	LIGHT_BLUE_CONCRETE_POWDER = LightBlueConcretePowder()
	LIGHT_BLUE_GLAZED_TERRACOTTA = LightBlueGlazedTerracotta()
	LIGHT_BLUE_SHULKER_BOX = LightBlueShulkerBox()
	LIGHT_BLUE_STAINED_GLASS = LightBlueStainedGlass()
	LIGHT_BLUE_STAINED_GLASS_PANE = LightBlueStainedGlassPane()
	LIGHT_BLUE_TERRACOTTA = LightBlueTerracotta()
	LIGHT_BLUE_WOOL = LightBlueWool()
	LIGHT_GRAY_CONCRETE = LightGrayConcrete()
	LIGHT_GRAY_CONCRETE_POWDER = LightGrayConcretePowder()
	LIGHT_GRAY_GLAZED_TERRACOTTA = LightGrayGlazedTerracotta()
	LIGHT_GRAY_SHULKER_BOX = LightGrayShulkerBox()
	LIGHT_GRAY_STAINED_GLASS = LightGrayStainedGlass()
	LIGHT_GRAY_STAINED_GLASS_PANE = LightGrayStainedGlassPane()
	LIGHT_GRAY_TERRACOTTA = LightGrayTerracotta()
	LIGHT_GRAY_WOOL = LightGrayWool()
	LIGHT_WEIGHTED_PRESSURE_PLATE = LightWeightedPressurePlate()
	LIME_CONCRETE = LimeConcrete()
	LIME_CONCRETE_POWDER = LimeConcretePowder()
	LIME_GLAZED_TERRACOTTA = LimeGlazedTerracotta()
	LIME_SHULKER_BOX = LimeShulkerBox()
	LIME_STAINED_GLASS = LimeStainedGlass()
	LIME_STAINED_GLASS_PANE = LimeStainedGlassPane()
	LIME_TERRACOTTA = LimeTerracotta()
	LIME_WOOL = LimeWool()
	LODESTONE = Lodestone()
	LOOM = Loom()
	MAGENTA_CONCRETE = MagentaConcrete()
	MAGENTA_CONCRETE_POWDER = MagentaConcretePowder()
	MAGENTA_GLAZED_TERRACOTTA = MagentaGlazedTerracotta()
	MAGENTA_SHULKER_BOX = MagentaShulkerBox()
	MAGENTA_STAINED_GLASS = MagentaStainedGlass()
	MAGENTA_STAINED_GLASS_PANE = MagentaStainedGlassPane()
	MAGENTA_TERRACOTTA = MagentaTerracotta()
	MAGENTA_WOOL = MagentaWool()
	MAGMA_BLOCK = MagmaBlock()
	MELON = Melon()
	MOSSY_COBBLESTONE = MossyCobblestone()
	MOSSY_COBBLESTONE_SLAB = MossyCobblestoneSlab()
	MOSSY_COBBLESTONE_STAIRS = MossyCobblestoneStairs()
	MOSSY_COBBLESTONE_WALL = MossyCobblestoneWall()
	MOSSY_STONE_BRICK_SLAB = MossyStoneBrickSlab()
	MOSSY_STONE_BRICK_STAIRS = MossyStoneBrickStairs()
	MOSSY_STONE_BRICK_WALL = MossyStoneBrickWall()
	MOSSY_STONE_BRICKS = MossyStoneBricks()
	MUSHROOM_STEM = MushroomStem()
	MYCELIUM = Mycelium()
	NETHER_BRICK_FENCE = NetherBrickFence()
	NETHER_BRICK_SLAB = NetherBrickSlab()
	NETHER_BRICK_STAIRS = NetherBrickStairs()
	NETHER_BRICK_WALL = NetherBrickWall()
	NETHER_BRICKS = NetherBricks()
	NETHER_GOLD_ORE = NetherGoldOre()
	NETHER_QUARTZ_ORE = NetherQuartzOre()
	NETHER_WART_BLOCK = NetherWartBlock()
	NETHERITE_BLOCK = NetheriteBlock()
	NETHERRACK = Netherrack()
	NOTE_BLOCK = NoteBlock()
	OAK_BUTTON = OakButton()
	OAK_FENCE = OakFence()
	OAK_FENCE_GATE = OakFenceGate()
	OAK_LEAVES = OakLeaves()
	OAK_LOG = OakLog()
	OAK_PLANKS = OakPlanks()
	OAK_PRESSURE_PLATE = OakPressurePlate()
	OAK_SLAB = OakSlab()
	OAK_STAIRS = OakStairs()
	OAK_TRAPDOOR = OakTrapdoor()
	OAK_WOOD = OakWood()
	OBSERVER = Observer()
	OBSIDIAN = Obsidian()
	ORANGE_CONCRETE = OrangeConcrete()
	ORANGE_CONCRETE_POWDER = OrangeConcretePowder()
	ORANGE_GLAZED_TERRACOTTA = OrangeGlazedTerracotta()
	ORANGE_SHULKER_BOX = OrangeShulkerBox()
	ORANGE_STAINED_GLASS = OrangeStainedGlass()
	ORANGE_STAINED_GLASS_PANE = OrangeStainedGlassPane()
	ORANGE_TERRACOTTA = OrangeTerracotta()
	ORANGE_WOOL = OrangeWool()
	PACKED_ICE = PackedIce()
	PETRIFIED_OAK_SLAB = PetrifiedOakSlab()
	PINK_CONCRETE = PinkConcrete()
	PINK_CONCRETE_POWDER = PinkConcretePowder()
	PINK_GLAZED_TERRACOTTA = PinkGlazedTerracotta()
	PINK_SHULKER_BOX = PinkShulkerBox()
	PINK_STAINED_GLASS = PinkStainedGlass()
	PINK_STAINED_GLASS_PANE = PinkStainedGlassPane()
	PINK_TERRACOTTA = PinkTerracotta()
	PINK_WOOL = PinkWool()
	PISTON = Piston()
	PODZOL = Podzol()
	POLISHED_ANDESITE = PolishedAndesite()
	POLISHED_ANDESITE_SLAB = PolishedAndesiteSlab()
	POLISHED_ANDESITE_STAIRS = PolishedAndesiteStairs()
	POLISHED_BASALT = PolishedBasalt()
	POLISHED_BLACKSTONE = PolishedBlackstone()
	POLISHED_BLACKSTONE_BRICK_SLAB = PolishedBlackstoneBrickSlab()
	POLISHED_BLACKSTONE_BRICK_STAIRS = PolishedBlackstoneBrickStairs()
	POLISHED_BLACKSTONE_BRICK_WALL = PolishedBlackstoneBrickWall()
	POLISHED_BLACKSTONE_BRICKS = PolishedBlackstoneBricks()
	POLISHED_BLACKSTONE_BUTTON = PolishedBlackstoneButton()
	POLISHED_BLACKSTONE_PRESSURE_PLATE = PolishedBlackstonePressurePlate()
	POLISHED_BLACKSTONE_SLAB = PolishedBlackstoneSlab()
	POLISHED_BLACKSTONE_STAIRS = PolishedBlackstoneStairs()
	POLISHED_BLACKSTONE_WALL = PolishedBlackstoneWall()
	POLISHED_DIORITE = PolishedDiorite()
	POLISHED_DIORITE_SLAB = PolishedDioriteSlab()
	POLISHED_DIORITE_STAIRS = PolishedDioriteStairs()
	POLISHED_GRANITE = PolishedGranite()
	POLISHED_GRANITE_SLAB = PolishedGraniteSlab()
	POLISHED_GRANITE_STAIRS = PolishedGraniteStairs()
	PRISMARINE = Prismarine()
	PRISMARINE_BRICK_SLAB = PrismarineBrickSlab()
	PRISMARINE_BRICK_STAIRS = PrismarineBrickStairs()
	PRISMARINE_BRICKS = PrismarineBricks()
	PRISMARINE_SLAB = PrismarineSlab()
	PRISMARINE_STAIRS = PrismarineStairs()
	PRISMARINE_WALL = PrismarineWall()
	PUMPKIN = Pumpkin()
	PURPLE_CONCRETE = PurpleConcrete()
	PURPLE_CONCRETE_POWDER = PurpleConcretePowder()
	PURPLE_GLAZED_TERRACOTTA = PurpleGlazedTerracotta()
	PURPLE_SHULKER_BOX = PurpleShulkerBox()
	PURPLE_STAINED_GLASS = PurpleStainedGlass()
	PURPLE_STAINED_GLASS_PANE = PurpleStainedGlassPane()
	PURPLE_TERRACOTTA = PurpleTerracotta()
	PURPLE_WOOL = PurpleWool()
	PURPUR_BLOCK = PurpurBlock()
	PURPUR_PILLAR = PurpurPillar()
	PURPUR_SLAB = PurpurSlab()
	PURPUR_STAIRS = PurpurStairs()
	QUARTZ_BLOCK = QuartzBlock()
	QUARTZ_BRICKS = QuartzBricks()
	QUARTZ_PILLAR = QuartzPillar()
	QUARTZ_SLAB = QuartzSlab()
	QUARTZ_STAIRS = QuartzStairs()
	RAIL = Rail()
	RED_CONCRETE = RedConcrete()
	RED_CONCRETE_POWDER = RedConcretePowder()
	RED_GLAZED_TERRACOTTA = RedGlazedTerracotta()
	RED_MUSHROOM_BLOCK = RedMushroomBlock()
	RED_NETHER_BRICK_SLAB = RedNetherBrickSlab()
	RED_NETHER_BRICK_STAIRS = RedNetherBrickStairs()
	RED_NETHER_BRICK_WALL = RedNetherBrickWall()
	RED_NETHER_BRICKS = RedNetherBricks()
	RED_SAND = RedSand()
	RED_SANDSTONE = RedSandstone()
	RED_SANDSTONE_SLAB = RedSandstoneSlab()
	RED_SANDSTONE_STAIRS = RedSandstoneStairs()
	RED_SANDSTONE_WALL = RedSandstoneWall()
	RED_SHULKER_BOX = RedShulkerBox()
	RED_STAINED_GLASS = RedStainedGlass()
	RED_STAINED_GLASS_PANE = RedStainedGlassPane()
	RED_TERRACOTTA = RedTerracotta()
	RED_WOOL = RedWool()
	REDSTONE_BLOCK = RedstoneBlock()
	REDSTONE_LAMP = RedstoneLamp()
	REDSTONE_ORE = RedstoneOre()
	REDSTONE_TORCH = RedstoneTorch()
	REPEATER = Repeater()
	REPEATING_COMMAND_BLOCK = RepeatingCommandBlock()
	RESPAWN_ANCHOR = RespawnAnchor()
	SAND = Sand()
	SANDSTONE = Sandstone()
	SANDSTONE_SLAB = SandstoneSlab()
	SANDSTONE_STAIRS = SandstoneStairs()
	SANDSTONE_WALL = SandstoneWall()
	SEA_LANTERN = SeaLantern()
	SHROOMLIGHT = Shroomlight()
	SHULKER_BOX = ShulkerBox()
	SLIME_BLOCK = SlimeBlock()
	SMITHING_TABLE = SmithingTable()
	SMOKER = Smoker()
	SMOOTH_QUARTZ = SmoothQuartz()
	SMOOTH_QUARTZ_SLAB = SmoothQuartzSlab()
	SMOOTH_QUARTZ_STAIRS = SmoothQuartzStairs()
	SMOOTH_RED_SANDSTONE = SmoothRedSandstone()
	SMOOTH_RED_SANDSTONE_SLAB = SmoothRedSandstoneSlab()
	SMOOTH_RED_SANDSTONE_STAIRS = SmoothRedSandstoneStairs()
	SMOOTH_SANDSTONE = SmoothSandstone()
	SMOOTH_SANDSTONE_SLAB = SmoothSandstoneSlab()
	SMOOTH_SANDSTONE_STAIRS = SmoothSandstoneStairs()
	SMOOTH_STONE = SmoothStone()
	SMOOTH_STONE_SLAB = SmoothStoneSlab()
	SNOW = Snow()
	SNOW_BLOCK = SnowBlock()
	SOUL_SAND = SoulSand()
	SOUL_SOIL = SoulSoil()
	SOUL_TORCH = SoulTorch()
	SPONGE = Sponge()
	SPRUCE_BUTTON = SpruceButton()
	SPRUCE_FENCE = SpruceFence()
	SPRUCE_FENCE_GATE = SpruceFenceGate()
	SPRUCE_LEAVES = SpruceLeaves()
	SPRUCE_LOG = SpruceLog()
	SPRUCE_PLANKS = SprucePlanks()
	SPRUCE_PRESSURE_PLATE = SprucePressurePlate()
	SPRUCE_SLAB = SpruceSlab()
	SPRUCE_STAIRS = SpruceStairs()
	SPRUCE_TRAPDOOR = SpruceTrapdoor()
	SPRUCE_WOOD = SpruceWood()
	STICKY_PISTON = StickyPiston()
	STONE = Stone()
	STONE_BRICK_SLAB = StoneBrickSlab()
	STONE_BRICK_STAIRS = StoneBrickStairs()
	STONE_BRICK_WALL = StoneBrickWall()
	STONE_BRICKS = StoneBricks()
	STONE_BUTTON = StoneButton()
	STONE_PRESSURE_PLATE = StonePressurePlate()
	STONE_SLAB = StoneSlab()
	STONE_STAIRS = StoneStairs()
	STONECUTTER = Stonecutter()
	STRIPPED_ACACIA_LOG = StrippedAcaciaLog()
	STRIPPED_ACACIA_WOOD = StrippedAcaciaWood()
	STRIPPED_BIRCH_LOG = StrippedBirchLog()
	STRIPPED_BIRCH_WOOD = StrippedBirchWood()
	STRIPPED_CRIMSON_HYPHAE = StrippedCrimsonHyphae()
	STRIPPED_CRIMSON_STEM = StrippedCrimsonStem()
	STRIPPED_DARK_OAK_LOG = StrippedDarkOakLog()
	STRIPPED_DARK_OAK_WOOD = StrippedDarkOakWood()
	STRIPPED_JUNGLE_LOG = StrippedJungleLog()
	STRIPPED_JUNGLE_WOOD = StrippedJungleWood()
	STRIPPED_OAK_LOG = StrippedOakLog()
	STRIPPED_OAK_WOOD = StrippedOakWood()
	STRIPPED_SPRUCE_LOG = StrippedSpruceLog()
	STRIPPED_SPRUCE_WOOD = StrippedSpruceWood()
	STRIPPED_WARPED_HYPHAE = StrippedWarpedHyphae()
	STRIPPED_WARPED_STEM = StrippedWarpedStem()
	TARGET = Target()
	TERRACOTTA = Terracotta()
	TNT = Tnt()
	TORCH = Torch()
	TRAPPED_CHEST = TrappedChest()
	TUBE_CORAL_BLOCK = TubeCoralBlock()
	WARPED_FENCE = WarpedFence()
	WARPED_FENCE_GATE = WarpedFenceGate()
	WARPED_BUTTON = WarpedButton()
	WARPED_HYPHAE = WarpedHyphae()
	WARPED_NYLIUM = WarpedNylium()
	WARPED_PLANKS = WarpedPlanks()
	WARPED_PRESSURE_PLATE = WarpedPressurePlate()
	WARPED_SLAB = WarpedSlab()
	WARPED_STAIRS = WarpedStairs()
	WARPED_STEM = WarpedStem()
	WARPED_TRAPDOOR = WarpedTrapdoor()
	WARPED_WART_BLOCK = WarpedWartBlock()
	WATER = Water()
	WET_SPONGE = WetSponge()
	WHITE_CONCRETE = WhiteConcrete()
	WHITE_CONCRETE_POWDER = WhiteConcretePowder()
	WHITE_GLAZED_TERRACOTTA = WhiteGlazedTerracotta()
	WHITE_SHULKER_BOX = WhiteShulkerBox()
	WHITE_STAINED_GLASS = WhiteStainedGlass()
	WHITE_STAINED_GLASS_PANE = WhiteStainedGlassPane()
	WHITE_TERRACOTTA = WhiteTerracotta()
	WHITE_WOOL = WhiteWool()
	YELLOW_CONCRETE = YellowConcrete()
	YELLOW_CONCRETE_POWDER = YellowConcretePowder()
	YELLOW_GLAZED_TERRACOTTA = YellowGlazedTerracotta()
	YELLOW_SHULKER_BOX = YellowShulkerBox()
	YELLOW_STAINED_GLASS = YellowStainedGlass()
	YELLOW_STAINED_GLASS_PANE = YellowStainedGlassPane()
	YELLOW_TERRACOTTA = YellowTerracotta()
	YELLOW_WOOL = YellowWool()
