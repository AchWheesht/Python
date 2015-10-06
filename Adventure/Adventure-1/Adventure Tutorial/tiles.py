import items, enemies, actions, world

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError()

	def modify_player(self, player):
		raise NotImplementedError()

	def adjacent_moves(self):
		"""Returns all move actions for adjacent tiles."""
		moves = []
		if world.tile_exists(self.x + 1, self.y):
			moves.append(actions.MoveEast())
		if world.tile_exists(self.x - 1, self.y):
			moves.append(actions.MoveWest())
		if world.tile_exists(self.x, self.y - 1):
			moves.append(actions.MoveNorth())
		if world.tile_exists(self.x, self.y + 1):
			moves.append(actions.MoveSouth())
		return moves

	def available_actions(self):
		"""Returns all of the available actions in this room."""
		moves = self.adjacent_moves()
		moves.append(actions.ViewInventory())

		return moves

class StartingRoom(MapTile):
	def intro_text(self):
		return """
		You find yoursself in a cave with a flickering torch on the wall.
		You can make out four paths, each equally as dark and forboding.
		You can't remember much about last night.

		Jesus, what the fuck were you drinking?
		"""

	def modify_player(self, player):
		#Room has no action on player
		pass

class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		super().__init__(x, y)

	def add_loot(self, player):
		player.inventory,append(self, item)

	def modify_player(self, player):
		self.add_loot(player)

class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)

	def modify_player(self, the_player):
		if self.enemy.is_alive():
			the_player.hp = the_player.hp - self.enemy.damage
			print("Your foe smacks you, and you watch {} pints of blood fly out the open gash. You reckon you have about {} pints of blood left")

	def available_actions(self):
		if self.enemy.is_alive():
			return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
		else:
			return self.adjacent_moves()

class EmptyCavePath(MapTile):
	def intro_text(self):
		return """
		There's not much in this part of the cave. You aren't sure whether this is a good or bad occurence
		"""

	def modify_player(self, player):
		#Room has no action on player
		pass

class PaulCroweRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.PaulCrowe())

	def intro_text(self):
		if self.enemy.is_alive():
			return """
			You find Paul unconcious here. Or at least, he was unconcious, and blissfully so, until you arrived.
			Now he's very much not unconcious, and very much not blissful, and very much about to gouge your eye's out with a corkscrew.
			"""
		else:
			return """
			Paul lies here, unconcious once more. You'll deal with him once you find a way out of this place."
			"""

class FindKeyboardRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.keyboard())

	def intro_text(self):
		return """
		You notice a keyboard in the middle of the room. What the fuck is a keyboard doing here?
		While there is no power for it, it's pretty heavy, and you reckon you could do some serious damage with it
		"""

class GavinLeechRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.GavinLeech())

	def intro_text(self):
		if self.enemy.is_alive():
			return """
			You find Gavin meditating in the middle of the room. You make to go and hello, but before you can, he stands up and draws his sword.

			He's clearly made a moral judgement, and decided that your existance makes the world a worse place. There's no stopping him now.
			"""
		else:
			return """
			Gavin lies dead in the middle of the room. You hope this doesn't cause the end of the world. Or, at least, you hope that your own continured presence doesn't
			"""

class JohnnyMorriceRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.JohnnyMorrice())

	def intro_text(self):
		if self.enemy.is_alive():
			return """
			As you walk into this paticular cave, you gasp for breath. It's beautiful! Sunlight streams through a hole in the ceiling, a little waterfall trickles past some flowers, squirrels and rabbit chitter merrily in the grass, and an enraged bearded programmer is charging towards you.

			Oh, fuck.
			"""
		else:
			return """
			Johnny's beardless corpse lies before you. You mourn for the now impossible sequel to get doomed".
			"""

class FindFistRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.Fist())

	def intro_text(self):
		return """
		Someone's fist is lying in the middle of this room. It looks a little better than your own, so you decide to use it as a weapon!
		"""

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True