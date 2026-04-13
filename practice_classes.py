#practice_classes

class User:
	def __init__(self,first,last,age):
		self.first = first
		self.last = last
		self.age = age
	
	def initials(self):
		return f"{self.first[0]} {self.last[0]}"

	def fullname(self):
		return f"{self.first} {self.last}"

	def is_senior(self):
		isSenior=False
		if (self.age>60):
			isSenior=True 
		return isSenior

	def likes(self,thing):
		self.thing = thing
		return f"{self.first} likes {self.thing}"
# user1 = User("tom", "sawyer",45)
# print (user1.initials())
# print (user1.is_senior())
# user2 = User("Mannie", "Attento",63)
# print (user2.initials())
# print (user2.is_senior())
# print (user1.likes("banana"))

class Vehicle:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model 
		self.year = year

		print ("a new car is ready with following features.. ")

		print (self.make)
		print (self.model)
		print (self.year)

# car1 = Vehicle("mercedes","s-class",2002)
# car2 = Vehicle("Vw","passat",2012)
# car3 = Vehicle("bmw","b-59",2008)
# car4 = Vehicle("skoda","x340",2004)

#print (f"name of the first car: {car1.__name__}")


class SocialMediaComments:
	def __init__(self,username,text,likes):
		self.name = username
		self.username = username
		self.text = text
		self.likes = likes 


# c = SocialMediaComments("davey123", "lol you're so silly", 3) 
# print (c.name)
# print (c.username)      #"davey123"
# print (c.text)       #"lol you're so silly"
# print (c.likes)        #3




class Person:
	def __init__(self):
		self.name="Tony"
		#self.last="Br"
		self._secret="hi!"
		self.__msg="911"
		self.__lol="you are so screwed!"
	def doorman(self, guess):
		if (guess == self._secret):
			print ("let them in...")


# p1 = Person()
# print (p1.name)
# p1.doorman("hi!")
# print (f"this is secret message: {p1._secret}")
# print (p1._Person__msg)
# print (p1._Person__lol)


class BankOwner:
	def __init__(self,name):
		self.owner = name
		self.balance=0.0

	def showBalance(self):
		return self.balance	

	def withdraw(self,amount):
		self.balance -= amount
		return self.balance

	def deposit(self,amount):
		self.balance += amount
		return self.balance


# b1 = BankOwner("Tom")

# print (b1.owner)
# print (b1.showBalance())
# b1.deposit(100)
# print(b1.showBalance())
# b1.withdraw(20)
# print (b1.showBalance())

#**********************************************************************************************************
#Exercise: using inheritance for facebook users 
#**********************************************************************************************************
class FacebookUsers:

	comment_list=[]
	active_users=0
	allowed_features = ["likes","comments","add_friends","message","post"]

	@classmethod
	def display_active_users(cls):
		return f"there are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls,data_str):
		first,last,age,requested_feature = data_str.split(",")
		print (first,last,age,requested_feature)
		return cls(first,last,int(age),requested_feature).__dict__


	def __init__(self,first,last,age,requested_feature):
		self.first = first
		self.last = last
		self.age = age
		self.requested_feature = requested_feature
		FacebookUsers.active_users+=1

		if (self.requested_feature not in FacebookUsers.allowed_features):
			#print (f"{self.first}: you cannot request a feature '{self.requested_feature}' that does not exist")
			raise ValueError(f"{self.first}: you cannot request a feature '{self.requested_feature}' that does not exist")
	# # destructor
	# def __del__(self):
	# 	print('Inside destructor')
	# 	print('Object destroyed')
	
	
	def __repr__(self):
		return f"{self.first} {self.last} is the facebook user"

	def initials(self):
		return f"{self.first[0]} {self.last[0]}"

	def fullname(self):
		return f"{self.first} {self.last}"

	def is_senior(self):
		isSenior=False
		if (self.age>60):
			isSenior=True 
		return isSenior

	def likes(self,thing):
		self.thing = thing
		return f"{self.first} likes {self.thing}"

	# def comments(self,comment):

	# 	if (isinstance(self,FacebookUsers)==True):
	# 		self.user_comment = comment
	# 		comment_dict = dict(name=self.first,comment=comment)
	# 		FacebookUsers.comment_list.append(comment_dict)
	# 	else:
	# 		print ("the user does not exist.. ")

	def comments(self,comment):
		if self == None:
			raise ValueError("the user does not exist")

		self.user_comment = comment
		comment_dict = dict(name=self.first,comment=comment)
		FacebookUsers.comment_list.append(comment_dict)
		
	def logout(self):
		print ("inside logout...")
		FacebookUsers.active_users-=1
		self = None
		#self.del



class Moderator(FacebookUsers):
	total_mods = 0
	def __init__(self,first,last,age,likes,community):
		super().__init__(first,last,age,likes)
		self.community = community
		Moderator.total_mods+=1

	@classmethod
	def display_active_mods(cls):
		return f"there are currently {cls.total_mods} active mods"

	@classmethod
	def from_string(cls,data_str):
		first,last,age,requested_feature,community = data_str.split(",")
		print (first,last,age,requested_feature,community)
		return cls(first,last,int(age),requested_feature,community).__dict__

	def __repr__(self):
		return f"{self.first} {self.last} is the FB moderator"

	def remove_post(self):
		return f"{self.fullname()} removed a post from {self.community}"


# user1 = FacebookUsers("Sujay","Rao",38,"likes")
# user2 = FacebookUsers("Tagline","Treichel",38,"likes")
# user3 =  Moderator("Sujay","Maithani",38,"post","Tennis")

# print (f"user1: {user1}")
# print (f"user2: {user2}")
# print (f"user3: {user3}")

# print ("-----------------------")
# # print (f"user1.fullname: {user1.fullname}")
# # print (f"user2.fullname: {user2.fullname}")
# # print (f"user3.fullname: {user3.fullname}")
# print (user1.fullname())
# print (user2.fullname())
# print (user3.fullname())

# print ("-----------------------")
# print (user1.from_string("Sujay,Rao,38,likes"))
# print (user2.from_string("Tagline,Treichel,38,likes"))
# print (user3.from_string("Sujay,Maithani,38,likes,Tennis"))

# print ("-----------------------")
# print (user3.remove_post())


# print ("-----------------------")
# print (FacebookUsers.display_active_users())
# print (Moderator.display_active_mods())

#***********************************************************************************************************************


# print (FacebookUsers.active_users)
# user1 = FacebookUsers("Sujay","Rao",38,"likes")
# user2 = FacebookUsers("Tagline","Treichel",38,"likes")
# print (FacebookUsers.active_users)
# user1.comments("I love eating banana")
# print (FacebookUsers.comment_list)
# user2.comments("I love eating cold pizza!")
# print (FacebookUsers.comment_list)
# print (FacebookUsers.display_active_users())


# user2.logout()
# print (FacebookUsers.active_users)
# print (user2.comments("I also love eating apples"))
# print (FacebookUsers.comment_list)
# print (FacebookUsers.active_users)
# print (FacebookUsers.display_active_users())


# user3 = FacebookUsers("Winston", "Churchill", 76, "post")
# user3.comments("I murdered millions of indians")
# print (FacebookUsers.comment_list)
# print (FacebookUsers.display_active_users())


# user4 = FacebookUsers.from_string("Albert,Einstein,95,likes")
# user4.comments("I am the most intelligent person on this planet")
# print (user4.fullname())
# print (FacebookUsers.comment_list)
# print (FacebookUsers.display_active_users())

#**********************************************************************************************************
#Exercise: using classes in poker 
#**********************************************************************************************************


from random import shuffle
class Card:
	def __init__(self,suit,value):
		self.suit = suit 
		self.value = value

	def __repr__(self):
		return f"{self.suit} of {self.value}"


class Deck:
	def __init__(self):
		suits = ["Hearts","Diamonds","Clubs","Spades"]
		values = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
		#self.cards = []
		self.cards = [Card(suit,value) for suit in suits for value in values]
		#print (self.cards)
		# for suit in suits:
		# 	for value in values:
		# 		#print (Card(suit,value))
		# 		self.cards.append(Card(suit,value))

		# print (self.cards)

	def __repr__(self):
		return f"Deck of {self.count()} cards"


	def count(self):
		return len(self.cards)

	def _deal(self,num):
		count = self.count()
		actual = min([count,num])
		print (f"going to remove {actual} cards")
		if count == 0:
			raise ValueError("all cards have been dealt with")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards

	def shuffle(self):
		#print (self.count())
		if (self.count()<52):
			raise ValueError ("only full decks can be shuffled")
		shuffle(self.cards)
		print (self.cards)
		return self

# # c = Card("Hearts","10")
# # print (c)

# d = Deck()
# #print (d.shuffle())
# print (d.shuffle())
# #print (d.cards)
# #print (d.cards)
# #print (d._shuffle())
# #print (d)
# #print (d._deal(4))
# #print (d.count())
# #print (d)

# # print (d._deal(52))
# # print (d._deal(3))




# class Animal:
# 	cool = True 


# 	def make_sound(self,sound):
# 		print (f"this animal says: {sound}")


# class Cat(Animal):
# 	pass

# a = Animal()
# a.make_sound("chirp")

# c = Cat()
# c.make_sound("meow")

# print (a.cool)
# print (Cat.cool)
# print (Animal.cool)
# print (f"is c is the instance of cat?: {isinstance(c,Cat)}")
# print (f"is a is the instance of cat?: {isinstance(a,Cat)}")
# print (f"is a is the instance of animal?: {isinstance(a,Animal)}")

#**********************************************************************************************************
#Using property for getting and setting values of attributes and methods 
#**********************************************************************************************************

class Human:
	def __init__(self,first,last,age):
		self.first = first
		self.last = last
		#self.age = age

		if (age > 0):
			self._age = age
		else:
			self._age = 0 


	# def get_age(self):
	# 	return self._age

	# def set_age(self,new_age):
	# 	if new_age >= 0:
	# 		self._age = new_age 
	# 	else:
	# 		self._age = abs (new_age)

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self,value):
		if (value>=0):
			self._age=value
		else:
			raise ValueError("age cannot be negative")

	@property		
	def fullname(self):
		return f"{self.first} {self.last}"

	@fullname.setter
	def fullname(self,name):
		self.first,self.last = name.split(" ")


# h1 = Human("Sujay","Rao",-30)
# print (h1)
# print (h1.age)
# h1.age=55
# print (h1.age)

# print (h1.fullname)
# h1.fullname = "Charles Xavier"
# print (h1.fullname)
# print (h1.__dict__)


# #print (h1.first, h1.last, h1.age)
# print (h1.get_age())
# h1.set_age(-39)
# print (h1.get_age())
# print (h1._age)

#**********************************************************************************************************
#Using super() inside inherited class
#**********************************************************************************************************

class Animal:
	def __init__(self,name,species):
		self.name = name 
		self.species = species

	def __repr__(self):
		return f"{self.name}  is a {self.species}"


	def make_sound(self,sound):
		return f"this animal says {sound}"


# class Cat(Animal):
# 	def __init__(self,name,species,breed,toy):
# 		self.name = name 
# 		self.species = species
# 		self.breed = breed
# 		self.toy = toy

# cat1 = Cat("sherkhan","Cat","Tiger","g-string")
# print (cat1)
# print (cat1.make_sound("grrrrrrrr"))

class Cat(Animal):
	def __init__(self,name,breed,toy):
		super().__init__(name,species="Cat")
		self.breed = breed
		self.toy = toy

	def play(self):
		return f"{self.name} plays with {self.toy}"

# cat1 = Cat("sherkhan","Tiger","g-string")
# print(cat1)
# print(cat1.make_sound("roar"))
# print(cat1.play())




#**********************************************************************************************************
#Exercise: inheritance 
#**********************************************************************************************************

class Character:
	def __init__(self,name,hp,level):
		self.name = name 
		self.hp = hp
		self.level = level

class NPC(Character):
	def __init__(self,name,hp,level):
		super().__init__(name,hp,level)

	def speak(self):
		#print ("I heard there were monsters lurking around last night!!!")
		return "I heard there were monsters lurking around last night!!!"

# villager = NPC("Jim",100,12)
# print (villager.name)
# print (villager.hp)
# print (villager.level)
# print (villager.speak())

#**********************************************************************************************************
#Multiple Inheritance 
#**********************************************************************************************************

class Aquatic:
	def __init__(self,name):
		print ("aquatic init")
		self.name = name
	def swim(self):
		return f"{self.name} is swimming"
	def greet(self):
		return f"I am {self.name} of the sea!"


class Ambulatory:
	def __init__(self,name):
		print ("ambulatory init")
		self.name = name
	def walk(self):
		return f"{self.name} is walking"
	def greet(self):
		return f"I am {self.name} of the land!"

class Penguin(Ambulatory,Aquatic):
	def __init__(self,name):
		print ("penguin init")
		super().__init__(name=name)
		Aquatic.__init__(self,name=name)
# aq = Aquatic("tuna")
# am = Ambulatory("turtle")
# ccook = Penguin("captain cook")
# print (Penguin.__mro__)
# print (Penguin.mro())
# help(Penguin)



# print (aq)
# print (aq.swim())
# print (aq.greet())

# print (am)
# print (am.walk())
# print (am.greet())

# print (pe)
# print (pe.walk())
# print (pe.greet())
# print (pe.swim())


# for num in [1,2,3]:
# 	print (num)
# for char in "hi there":
# 	print (char)


from random import choice 

def greet(person):
	def get_mood():
		mood = choice(("hello","I am not in a good mood", "I am angry right now..","get the fuck out.."))
		return mood
	result = person + ": " +get_mood() 
	return result
	#return get_mood
# print (greet("Sujay"))
# print (which_mood())
# which_mood = greet("Vijay")
# print (which_mood())



def make_laugh_func():
	def get_laugh():
		l = choice(("hello","I am not in a good mood", "I am angry right now..","get the fuck out.."))
		return l
	return get_laugh

# laugh = make_laugh_func()
# print (laugh())

print ("-------------------------------------------------------------------")


def make_laugh_at_func(person):
	def get_laugh():
		mood = choice(("hello","I am not in a good mood", "I am angry right now..","get the fuck out.."))
		return f"{person}:{mood}"
	return get_laugh

# laugh_at = make_laugh_at_func("Sujay")

# for i in range(1,5):
# 	print (laugh_at())


def be_polite(fn):
	def wrapper():
		print("what a pleasure to meet you")
		fn()
		print ("have a great day")
	return wrapper

def greet():
	print ("my name is colt..")

def rage():
	print ("I am angry!")

# greet = be_polite(greet)
# rage = be_polite(rage)

# greet()
# rage()







def be_polite(fn):
	def wrapper():
		print ("what a pleasure to meet you!")
		fn()
		print ("have a great day!")
	return wrapper

@be_polite
def amazing():
	print ("I am feeling amazing!")

@be_polite
def rage():
	print ("I am in rage!")

# amazing()
# rage()





def shout(fn):
	def wrapper(*args,**kwargs):
		return fn(*args,**kwargs).upper()
	return wrapper

@shout
def greet(name):
	return f"Hi, I am {name}"

@shout
def order(main,side):
	return f"I would like the {main}, with the {side} please"

# print (greet("sujay"))
# print (order("chicken curry","salad"))



def log_function_data(fn):
	def wrapper(*args,**kwargs):
		print (f"you are about to call: {fn.__name__}")
		print (f"you are about to call: {fn.__doc__}")
		return fn(*args,**kwargs)
	return wrapper


@log_function_data
def add(x,y):
	'''Adds two numbers together'''
	return x+y 

# print (add(10,40))



from functools import wraps
from time import time 

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args,**kwargs):
		start_time = time()
		result = fn(*args,**kwargs)
		end_time = time()
		print (f"time elapsed = {end_time - start_time}")
		return result
	return wrapper

@speed_test
def sum_nums_gen():
	return sum(x for x in range(1,1000000))

@speed_test
def sum_nums_list():
	return sum([x for x in range(1,1000000)])


# print (sum_nums_gen())
# print (sum_nums_list())

#from functools import wraps

def show_args(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
	    print("Here are the args:", args)
	    print("Here are the kwargs:", kwargs)
	    return fn(*args, **kwargs)
	return wrapper

@show_args
def greet1(name):
	return f"Hi, I am {name}"

@show_args
def order1(main,side):
	return f"I would like the {main}, with the {side} please"


# print (greet1("sujay"))
# print (order1("chicken curry","salad"))

from functools import wraps

def ensure_no_kwargs(fn):
	@wraps(fn)
	def wrapper(*args,**kwargs):
		if kwargs:
			raise ValueError("No kwargs allowed sorry!")
		return fn(*args,**kwargs)
	return wrapper

@ensure_no_kwargs
def greet(name):
	print (f"hi there! {name}")


# greet("Tony")
# greet(name="Tony")



# from functools import wraps
 
# def double_return(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         val = fn(*args, **kwargs)
#         return [val, val]
#     return wrapper


# @double_return
# def func_with_args(name,age):
# 	print (f"hi there! {name} with age {age}")

# print (func_with_args(name="Sujay",age=39))



from functools import wraps

def ensure_fewer_than_three_args(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
	    if len(args) < 3:
	    	return fn(*args, **kwargs)
	    return "Too many arguments!"
	return wrapper

@ensure_fewer_than_three_args
def func_with_args(name,age,city,nationality):

	return f"{name}:{age}:{city}:{nationality}"


#print (func_with_args(name="Sujay",age=39, city="Kaiserslautern",nationality="German"))


#print (func_with_args(name="Sujay",age=39, city="Kaiserslautern",nationality="German"))

from functools import wraps

def only_ints(fn):
	@wraps(fn)
	def inner(*args, **kwargs):
	    if any([arg for arg in args if type(arg) != int]):
	        return "Please only invoke with integers."
	    return fn(*args, **kwargs)
	return inner

@only_ints
def func_with_ints(arg1,arg2):
	return arg1+arg2

# print (func_with_ints("Sujay",3))



from functools import wraps
 
def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper

@ensure_authorized
def check_role(name,role):
	return f"Access verified for {name} with {role}"

print (check_role(name="Sujay",role="user"))




