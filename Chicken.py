class Chicken:
    total = 0
    def __init__(self,name,eggs=0):
        self.name = name 
        self.eggs = eggs
    def lay_egg(self):
        self.eggs+=1
        Chicken.total+=1
        supra="st"
        if (self.eggs == 1):
            supra="st"
        elif (self.eggs == 2):
            supra="nd"
        elif (self.eggs == 3):
            supra="rd"
        else:
            supra="th"
        print (f"{self.name} has layed {self.eggs}{supra} egg")

c1 = Chicken("vijay")
c2 = Chicken("Panda")
c1.lay_egg()
c1.lay_egg()
c1.lay_egg()
c1.lay_egg()
c1.lay_egg()
c2.lay_egg()
c2.lay_egg()

print (f"There are total of {Chicken.total} eggs")
