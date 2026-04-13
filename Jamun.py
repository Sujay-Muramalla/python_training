class Jamun:
    def __init__(self,color,size,age):
        self.color=color
        self.size=size
        self.age=age
        print (f"the characteristics of jamun {self} are as follows -- color: {self.color}, size:{self.size}, age: {self.age} ")

j1 = Jamun("red",10,4)
j2 = Jamun("yello",8,34)
j3 = Jamun("green",3,89)
j4 = Jamun("blue", 5, 98)
j5 = Jamun("gray",7,78)



print (j1,j2,j3,j4,j5)

print (f"this is the color of j4: {j4.color}")
