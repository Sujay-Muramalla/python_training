class Human:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last

        
        if age >= 0:
            self._age = age
        else:
            self._age = 0
            
    # def get_age(self):
    #     return self._age
    
    # def set_age(self,new_age):
    #     if new_age>=0:
    #         self._age = new_age
    #     else:
    #         self._age = 0
    #     print (f"the new age is set: {self._age}")

    def display_fullname(self):
        fullname = self.first + self.last
        return fullname

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if value >= 0:
            self._age = value
        else:
            self._age = 0
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    @full_name.setter
    def full_name(self,name):
        self.first,self.last = name.split(" ")
        
        

print ("--------------------------------------------")
    
h1 = Human("sujay","rao",41)
print (h1._age)
print (h1.display_fullname())

print ("--------------------------------------------")

#example accessing and modifying the age property directly
h1._age=54
print (h1._age)
print (h1.display_fullname())


print ("--------------------------------------------")
# #example for modifying the age using set_age method
# h1.set_age(66)
# print (h1.get_age())

print (f"using @property annotations..")
h1.age=20
print (h1.age)


print ("--------------------------------------------")
h1.full_name = "Sujay Muramalla"
print (h1.full_name)
print (h1.__dict__)
