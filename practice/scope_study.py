def update_health(amount):
	monster.health += amount


# health = 10
# print(health)
# update_health(20)

class Monster:
	def __init__(self,health,energy):
		self.health = health
		self.energy = energy

	def update_energy(self,amount):
		self.energy += amount

	def get_damage(self,amount):
		self.health -= amount

class Hero:
	def __init__(self,damage,monster):
		self.damage = damage
		self.monster = monster

	def attack(self):
		self.monster.get_damage(self.damage)


monster = Monster(health =100, energy =50)
print(monster.health, monster.energy)
hero = Hero(damage = 15,monster = monster)
hero.attack()
print(monster.health)