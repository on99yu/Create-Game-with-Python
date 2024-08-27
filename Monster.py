class Monster():
	health = 90
	energy = 40
	def attack(self, amount):
		print("The monster has attacked")
		print(f'{amount} damage was dealt')
		monster.energy -= 20
		print(monster.energy)

	def move(self,speed):
		print('The monster has moved')
		print(f'It has a speed of {speed}')

monster = Monster()
monster1 = Monster()
monster.attack(40)
monster1.move(10)