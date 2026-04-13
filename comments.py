class Comment:
    def __init__(self, username, text, likes=0):
        self.username=username
        self.text=text
        self._likes=likes 
        self._secret="Red Apple ahead"
        self.__secret_msg="waterfall"
        
        print (f"{username} says..{text}. the text has now {likes} likes")
        
    def evacuate(self,doorcode):
        if doorcode==self._secret:
            print ("troops recede...i repeat, troops recede...")
            return 1
        return 0
    def check_likes(self,no_of_likes):
        if (no_of_likes>self._likes):
            print (f"you assumed greater likes which is: {no_of_likes}..., the actual likes were{self._likes}")
            
        else:
            print (f"you assumed less...than {self._likes}")
            
    def attack(self,warcode):
        if (warcode == self.__secret_msg):
            print (f"Code is {self.__secret_msg}...attack")
            
    def say_hi():
        print ("hello")
        
        
u1 = Comment("user1","this cute girl is so adorable..",10)
u2 = Comment("user2","the pic is fab..")
print (u1._secret)
operation_exit_code = u1.evacuate("Red Apple ahead")
if (operation_exit_code == 1 ):
    print (f"evacuation succeeeded... for {u1.username}")
else:
    print (f"operation failed ...for {u1.username}")

u1.check_likes(5)
u1.check_likes(11)
u1.check_likes(8)
u1.check_likes(0)
#print (u1.__secret_msg)
u1.attack("waterfall")
print (dir (u1))
print (u1._Comment__secret_msg)
u1.say_hi()