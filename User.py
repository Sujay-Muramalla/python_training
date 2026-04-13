#define class user
class User:
	def __init__(self,firstname,lastname,age):
		self.firstname=firstname
		self.lastname=lastname
		self.age=age

	def fullname(self):
		return f"{self.firstname} {self.lastname}"

	def likes(self, food):
		print (f"{self.firstname} likes {food}")


user1 = User("sujay","muramalla",38)
user2 = User("tagline", "treichel", 38)


print (user1.fullname)
print (user2.fullname)
print (user1.likes("ice cream"))
print (user2.likes("mango"))