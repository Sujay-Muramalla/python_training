from os import name


class Mother:
    def __init__(self, name="Sai Sitara"):
        print (f"this is Mother Init method")
        #self.name = name
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"
        print (f" Mother's name is {name} hair color is {self.hair_color} and hair type is {self.hair_type}")
 
 
class Father:
    def __init__(self, name="Mahi"):
        print (f"this is Father Init method")
        self.name = name
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"
        print (f" Father's name is {self.name} hair color is {self.hair_color} and hair type is {self.hair_type}")

 
class Child(Mother, Father):
    
    def __init__(self,name):
        super().__init__()
        self.name = name
       
        
    def __repr__(self):
        return f"Child's name is {self.name}, eye color is {self.eye_color}, hair color is {self.hair_color}, and hair type is {self.hair_type}"
    


m = Mother("Sai Sitara")
f = Father("Mahi")


print ("-----------------MRO---------------------------")
print (Child.mro())
c = Child("Sujay")
print (f"c.name: {c.name}")
print (c)
