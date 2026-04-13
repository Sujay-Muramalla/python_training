#Weapons.py

class Weapons:
	

	allowed_weapons = ["trishul","pinaka","agni","brahmos","prithvi","nag","akash"]
	def __init__(self,type_of_weapon,number_of_fires):
		self.type = type_of_weapon
		self.number_of_fires = number_of_fires
		print (f"A new weapon of type {self.type} with {self.number_of_fires} rounds of fires has been created")

	def weapon_name(self,name):
		self.name = name
		print (f"{self.name} has been requested")
		if (self.name not in Weapons.allowed_weapons):
			raise ValueError(f"the weapon name {self.name} does not exist and cannot be assigned")
		return f"you have acquired now {self.name}"

	def shoot(self):
		print (f"{self.name} has been fired")


	def weapon_description(self):
		if (self.name == "trishul"):
			print (f"{self.name} is nuclear")
		if (self.name == "pinaka"):
			print (f"{self.name} is nuclear and multi ballistic")
		if (self.name == "akash"):
			print (f"{self.name} is air to air short range auto target missile")

	def is_dangerous(self):
		if (self.number_of_fires> 80):
			print (f"{self.name} is dangerous")
		else:
			print (f"{self.name} can cause midrange destruction")

w1 = Weapons("surface_to_air",100)
w2 = Weapons("surface_to_surface",60)
w3 = Weapons("air to air",70)

print (w1)
print (w2)
print (w3)

w1_trishul = w1.weapon_name("trishul")
w2_pinaka = w2.weapon_name("pinaka")
w3_akash = w3.weapon_name("akash")

print (w1_trishul)
print (w2_pinaka)

w1.shoot()
w2.shoot()

w1.weapon_description()
w2.weapon_description()

w1.is_dangerous()
w2.is_dangerous()
