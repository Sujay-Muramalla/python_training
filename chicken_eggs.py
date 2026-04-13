#chickenandeggs.py
class Chicken:
    eggs=0
    total_eggs=0
    def __init__(self,name,species):
        self.name=name 
        self.species=species
    
    def lay_egg(self):
        self.eggs+=1
        self.total_eggs+=1
        return self.eggs
        

c1 = Chicken("manish", "murga")
c2 = Chicken("zuber","cocky")
c3 = Chicken("Tapan","bandar murga")


c1.lay_egg()
c1.lay_egg()
c2.lay_egg()
c2.lay_egg()
print (c1.total_eggs)
print (c1.eggs)
print (c2.total_eggs)
print (c2.eggs)



#Here's my implementation of the Chicken class.  Notice the total_eggs class attribute.
class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0
    
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs