class Monster():

	def __init__(self,health,energy):
		self.health = health
		self.energy = energy 

	def __len__(self):
		return self.health
	def __abs__(self):
		return self.energy
	def __call__(self):
		return "The monster was called "
	def __add__(self,other):
		return self.health+other
	def __str__(self):
		return f"A monster with health {self.health} and energy {self.energy}"
	
	def attack(self, amount):
		print("The monster has attacked")
		print(f'{amount} damage was dealt')
		self.energy -= 20

	def move(self,speed):
		print('The monster has moved')
		print(f'It has a speed of {speed}')

# monster1 = Monster(10,20)
# print(monster1.health)
# print(monster1.__dict__)
# print(monster1 + 55 )
# print(monster1)

class Shark(Monster):
	def __init__(self,speed, health, energy):
		# Monster.__init__(self, health, energy)
		super().__init__(health, energy)
		self.speed = speed

	def bite(self):
		print("The shark has bitten")
	def move(self):
		print('The shark has moved')
		print(f'The speed of the shark is {self.speed}')

class Scorpion(Monster):
	def __init__(self,poison_damage,scorpion_health, scorpion_energy):
		super().__init__(health=scorpion_health, energy=scorpion_energy)
		self.poison_damage = poison_damage

	def attack(self):
		print(f"Scorpion has attacked \nIt has dealt {self.poison_damage} poison_damage ") 

shark = Shark(speed = 120, health=100, energy =80 )
shark.move()
print(shark.speed)
scorpion = Scorpion(50,20,10)
scorpion.attack()
scorpion.move(5)
print(scorpion.health)