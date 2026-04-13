class Aquatic:
    def __init__(self, name):
        print ("AQUATIC INIT")
        self.name = name
        print(f"this is aquatic class: {self.name}")

    def swim(self):
        print(f"{self.name} is swimming.")
        
    def greet(self):
        print(f"{self.name} says hello from the water!")

class Ambulatory:
    print ("AMBULATORY INIT")
    def __init__(self, name):
        self.name = name
        print(f"this is ambulatory class: {self.name}")

    def walk(self):
        print(f"{self.name} is walking.")
        
    def greet(self):
        print(f"{self.name} says hello from the land!")

class Multi(Ambulatory, Aquatic):
    def __init__(self, name, breed, age):
        print ("MULTI INIT")
        #super().__init__(name=name)
        Ambulatory.__init__(self, name)
        Aquatic.__init__(self, name)
        self.breed = breed
        self.age = age
        print (f"this is multi class, name: {name}")
        print (f"this is multi class, self.name: {self.name}")
        print (f"this is multi class, breed: {breed}")
        print (f"this is multi class, age: {age}")


# aq = Aquatic("Dolphin")
# am = Ambulatory("Dog")
# pe = Multi("Duck","Mallard", 2)

# print (f"--------------printing attributes of aquatic and ambulatory-----------")
# aq.swim()
# am.walk()

# print (f"--------------printing attributes of penguin-----------")
# pe.greet()
# print (pe.breed)
# print (pe.age)
# print (pe.name)

pe = Multi("Duck", "Mallard", 2)

