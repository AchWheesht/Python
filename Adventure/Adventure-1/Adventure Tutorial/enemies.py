class Enemy:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def is_alive(self):
		return self.hp > 0

class PaulCrowe(Enemy):
	def __init__(self):
		super().__init__(name="Paul Crowe, Destroyer of Bottles", hp = 20, damage = 2)

class GavinLeech(Enemy):
	def __init__(self):
		super().__init__(name="Gavin Leech, the Unaware", hp = 30, damage = 1)

class JohnnyMorrice(Enemy):
	def __init__(self):
		super().__init__(name="Johnny Morrice, J-punk Superstar", hp = 20, damage = 5)
	
