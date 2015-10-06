class Item():
		"""The base class for all items"""
		def __init__(self, name, description, value):
			self.name = name
			self.description = description
			self.value = value

		def __str__(self):
			return "{}\n=====\n{}\nvalue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
	def __init__(self,amt):
		self.amt = amt
		super().__init__(name="Gold",
			description="A round coin with {} stamped on the front.".format(str(self.amt)),
			value=self.amt)

class Weapon(Item):
	"""The subclass for all weapons"""
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
	def __init__(self):
		super().__init__(name="Rock",
			description="A rock. But not a very good rock.",
			value=0,
			damage=1)

class Fist(Weapon):
	def __init__(self):
		super().__init__(name="Fist",
				description="Someone's fist. You don't know whose, but hey, at least it's not yours",
				value=1,
				damage=5)

class Keyboard(Weapon):
	def __init__(self):
		super().__init__(name="Keyboard",
				description="A disused keyboard. It doesn't seem to work, but it's heavy and got some reach on it",
				value=5,
				damage=10)

