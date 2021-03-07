class GameRules:
	"""
	A list of gamerules used by the world.
	Contains all gamerules for Java edition as of 1.16.5.
	"""

	def __init__(self):
		"""
		Creates the rules of the class.
		"""

		self.rules = []
		self.create_game_rules()

	
	def create_game_rules(self):
		"""
		Saves every gamerule to the self.rules array.
		"""

		self.rules.extend([
			{
				"name": "announceAdvancements",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "commandBlockOutput",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "disableElytraMovementCheck",
				"value": "false",
				"type": "bool"
			},
			{
				"name": "disableRaids",
				"value": "false",
				"type": "bool"
			},
			{
				"name": "doDaylightCycle",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "doEntityDrops",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "doFireTick",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "doInsomnia",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "doImmediateRespawn",
				"value": "false",
				"type": "bool"
			},
			{
				"name": "doLimitedCrafting",
				"value": "false",
				"type": "bool"
			},
			{
				"name": "doMobLoot",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "doMobSpawning",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "doPatrolSpawning",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "doTileDrops",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "doTraderSpawning",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "doWeatherCycle",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "drowningDamage",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "fallDamage",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "fireDamage",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "forgiveDeadPlayers",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "freezeDamage",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "keepInventory",
				"value": "false",
				"type": "bool"
			},
			{
				"name": "logAdminCommands",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "maxCommandChainLength",
				"value": "65536",
				"type": "int"
			},
			{
				"name": "maxEntityCramming",
				"value": "24",
				"type": "int"
			},
			{
				"name": "mobGriefing",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "naturalRegeneration",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "playersSleepingPercentage",
				"value": "100",
				"type": "int"
			},
			{
				"name": "randomTickSpeed",
				"value": "3",
				"type": "int"
			},
			{
				"name": "reducedDebugInfo",
				"value": "false",
				"type": "bool"
			},
			{
				"name": "sendCommandFeedback",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "showDeathMessages",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "spawnRadius",
				"value": "10",
				"type": "int"
			},
			{
				"name": "spectatorsGenerateChunks",
				"value": "true",
				"type": "bool"
			},
			{
				"name": "universalAnger",
				"value": "false",
				"type": "bool"
			}
		])

	
	def set_rule(self, name, value):
		"""
		Sets a rule. The value must be the type (bool, int) of the gamerule.

		:param name: the name of the rule
		:param value: the value to set the rule to
		"""

		for rule in self.rules:
			if rule["name"] == name:
				if rule["type"] == "bool" and not isinstance(value, bool):
					raise ValueError("Given value is not of correct type")
				elif not isinstance(value, int):
					raise ValueError("Given value is not of correct type")

				rule["value"] = str(value).lower()
				return True

		raise ValueError(f"Game rule {name} could not be found")

