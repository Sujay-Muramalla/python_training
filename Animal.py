class Animal():

	def __init__(self,name,species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self,sound):
		print (f"this animal says : {sound}")

	def eat(self,food):
		print (f"I eat {food}")


class Cat(Animal):
	def __init__(self,name,species,breed,toy):
		super().__init__(name,species)
		self.breed = breed
		self.toy = toy

	def eat(self,food):
		print (f"I eat: {food}")




a = Animal("daffy","Duck")
print(a)
a.make_sound("quack")

c = Cat("tom","panthera","pet cat","box")
#c = Cat("pet cat","box")
print (c)
c.make_sound("mmeeeeow")
c.eat("fish")

print (c.breed)
print (c.toy)