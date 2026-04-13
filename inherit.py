class Animal:
    
    def __init__(self,legs,arms,eyes,skin,hair):
        self.legs = legs
        self.arms = arms 
        self.eyes = eyes
        self.skin = skin 
        self.hair = hair
    
    def __repr__(self):
        return f"Repr: an animal is created with {self.legs} legs, {self.arms} arms, {self.eyes} eyes, with {self.skin} skin and {self.hair} hair"
    
    def displayCharacts(self):
        print (f"the animal has {self.legs} legs, {self.arms} arms, {self.eyes} eyes, with {self.skin} skin and {self.hair} hair")
    
    def make_sound(self,sound):
        print (f"this animal says {sound}")
    

class Cat(Animal):
    
    def furcolor(self,color):
        print (f"the cat's color is {color}")

c = Cat(2,2,2,"brown","black")
print (c)
c.displayCharacts()
c.make_sound("meow")
c.furcolor("blue")

