# pymcworld
`pymcworld` is a simple world creator for Minecraft. It currently supports 1.16.5. The library automatically takes care of level files, placing of blocks, gamerules, and more. It currently supports over 500 blocks.
Example:

    from pymcworld.world import World

	world = World()
	world.set_block(0, 0, 0, world.blocks.ANDESITE)
	world.save("testworld")

This creates a world, with the block at (0, 0, 0) set to andesite, and saves the world to the `testworld` folder. This is the code to create a sphere:

    from pymcworld.world import World

	world = World()
	# this function takes 5 arguments: x, y, z, radius, and block type
	world.shape.sphere(0, 20, 0, 15, world.blocks.ANDESITE)
	world.save("testworld")
