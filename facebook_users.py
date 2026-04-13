#facebook_users.py

class User:


	active_users=0
	def __init__(self,first,last,age):
		self.first =  first
		self.last = last
		self.age = age
		User.active_users+=1
	
	def fullname(self):
		return f"{self.first} {self.last}"
	def initials(self):
		return f"{self.first[0] , self.last[0]}"
	def is_senior(self):
		return self.age >= 65

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def birthday(self):
		self.age+=1
		return f"happy {self.age}th birthday"

	def logout(self):
		User.active_users-=1
		print (f"{self.first} {self.last} has logged out")
		print (f"{User.active_users} users are currently active..")



user1 = User("sujay","muramalla",39)
user2 = User("tagline", "treichel", 39)
user3 = User("chris", "benz", 23)

print (user1.fullname())
print (user2.fullname())
print (user3.fullname())

print (user1.likes("dal"))
print (user2.likes("steak"))
print (user3.likes("kebap"))

#print (User.active_users)

user1.logout()
#print (User.active_users)