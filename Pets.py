class Pets:
    allowed = ['cat','dog','fish','rabbit','rat']
    
    @classmethod
    def displayAllowed(cls):
        return f"the allowed pets are: {cls.allowed}"
    
    
    def __init__(self,name, species):
        self.name = name
        self.species = species
        if species not in Pets.allowed:
            raise ValueError(f"{self.species} is not allowed")
            #print (f"{self.species} is not allowed")
            exit (0)
    
    def welcome(self):
        print (f"Your pet {self.name} of species {self.species} is Welcome")
        
    def set_species(self,species):
        #self.species = species
        if species not in Pets.allowed:
            #raise ValueError(f"you cannot have {species} pet")
            print (f"you cannot have {species} as a pet")
            #exit(0)
        self.species = species
    
    def eat(self,food):
        print (f"I eat {food}")
    

p1 = Pets('tom','cat')
p2 = Pets('jerry','rat')
#p3 = Pets('nagraj','snake')
p1.eat("fish")

p1.welcome()
#p3.welcome()
p2.welcome()
#p3.species = "Snake"
#p3.welcome()
p1.set_species("dragon")
p1.welcome()

p1.species = "tiger"
p1.welcome()
print (p1.allowed)
print (p2.allowed)
p2.allowed = ['horse','deer','elephant']
print (p2.allowed)
print (p1.allowed)
p2.welcome()
p1.welcome()


print ("............Printing Class Attribute Allowed........")
print (Pets.allowed)

if "Reptile" not in Pets.allowed:
    Pets.allowed.append("Reptile")
    
print (Pets.allowed)
new_pet = Pets("Lizard","Reptile")
print (new_pet.name)
print (new_pet.species)

x = new_pet.displayAllowed()
print (x)

