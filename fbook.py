class User:
    active_users=0
    @classmethod
    def display_active_users(cls):
        print (cls)
        return f"there are currently {cls.active_users} active users"
    
    @classmethod
    def from_string(cls,data_str):
        name,age = data_str.split(",")
        print (f"inside from_string method, print (name,age): {name,age}")
        return cls(name,age)
    
    def __init__(self,uname,age):
        self.uname = uname
        self.age = age
        User.active_users+=1
    
    
    def __repr__(self):
        return f"{self.uname} is {self.age} years old"
    
    def welcome(self):
        supra="th"
        if (User.active_users == 1):
            supra="st"
        elif (User.active_users == 2):
            supra="nd"
        elif (User.active_users == 3):
            supra="rd"
        else:
            supra="th"
        
        print (f"welcome {self.uname} to fbook. You are the {User.active_users}{supra} user of fbook")
    
    def displayAge(self):
        print (f"Dear {self.uname}, as per our entries, your mentioned age is {self.age} ")
        
    def logout(self):
        User.active_users -= 1
        print (f"Dear {self.uname}, you have logged out of fbook")

u1 = User("Sujay",41)
u2 = User("Akash",41)
u3 = User("Prajesh",41)
u4 = User("Deepesh",41)
u5 = User("Dengesh",41)
print (u1)
print (u2)



u1.welcome()
u1.displayAge()
u2.welcome()
u2.displayAge()
u3.welcome()
u3.displayAge()
u4.welcome()
u4.displayAge()
u5.welcome()
u5.displayAge()



print (User.active_users)

u1.logout()
u2.logout()
u3.logout()

print(f"Printing here User.active_users: {User.active_users}")
print ("here we print class method.....")
print ("---------------------------------------")
print (User.display_active_users())

print ("----------------------------------------")
print ("testing class method on from_string")
print ("----------------------------------------")

sujay = User.from_string("Sujay,354")
print(sujay.uname)
#print (sujay.name)
print (sujay.age)
#print (sujay.name)
sujay.displayAge()

