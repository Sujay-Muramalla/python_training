#Chicken_Soup.py

class Chicken:

	total_eggs=0
	def __init__(self,name,species):
		self.eggs=0
		self.name=name
		self.species=species


	def lay_egg(self):
		self.eggs+=1
		Chicken.total_eggs+=1
		return self.eggs

	def speak(self, time=""):
		if (time == "18:00"):
			print ("cuckdukoooooooooooooooooooooooooooooooooooo!")
		else:
			print ("ko ko kok  kok o")

c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")

c1.lay_egg()
c2.lay_egg()

c1.lay_egg()
c1.lay_egg()
c2.lay_egg()
c2.lay_egg()
c2.lay_egg()
c2.lay_egg()
c2.lay_egg()
c2.lay_egg()
c2.lay_egg()

print (c1.total_eggs)
print (c1.eggs)
print (c2.total_eggs)
print (c2.eggs)

c1.speak("18:00")
c2.speak()









