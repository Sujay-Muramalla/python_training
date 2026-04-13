from random import choice
class Laugh:
    def __init__(self,name):
        self.name = name
        
    
    def __repr__(self):
        return f"hello {self.name}, you are welcome to the world of laughter!"

    def get_laugh(self):
        laugh = choice(("hahahaha", "hohoho","kkkkkkk","hehehehehehehe"))
        return laugh
    
    def get_message(self):
        msg = f"{self.name} you are crazy hilarious. {self.get_laugh()}"
        return msg
    
l1 = Laugh("Sujay")
print (l1)
#x = l1.get_message()
#print (x)

for i in range(10):
    print (l1.get_message())
