#class_practice.py
class Players:

	#declare class attribute
	active_players = 0
	#age here is by default 20, if none is given while instantiating the class. 

	#define classmethod to display number of active players. 
	@classmethod
	def display_active_players(player_class):
		#print (player_class)
		return f"there are currently {player_class.active_players} active players"

	@classmethod
	def from_string(player_class,data_str):
		name,likes,age = data_str.split(",")
		return player_class(name,likes,age)

	def __init__(self,name,likes,age=20):
		#define instance attributes here, which are automatically initialized. 
		self.name = name
		self.likes = likes
		self.age = age
		Players.active_players+=1
		#SUVs 
		self._role = "gamer" #NameError: name 'role' is not defined
		self._last = "rao"
		
		#DUVs
		self.__msg = "this is the player class, there are some secrets in it. You need to know whom to ask!;)"
		self.__lol = "hahahahhahahahahah ... this is a fake class"

		print (f"{self.name} likes {self.likes} and has age {self.age}")

	#demonstration of single underscore variables: _role 
	#SUVs such as _role are used like private variables although python does not have concept of private
	#they are meant for use by instance methods of the class. 
	def player_role (self,role_info): #instance method
		print (f"inside player_role(): the value of self._role: {self._role}")
		if role_info == self._role: #role_info is being compared privately with _role in Player class. If it matches, the output says "serious gamer"
			print (f"{self.name} is a serious gamer")
		else:
			print (f"{self.name} is a {role_info}")

	def add_last (self,last):
		self._last = last
		return self._last

	def player_fullname(self):
		return f"{self.name} {self._last}"

	def player_initials(self):
		return f"player initials are: {self.name[0].upper()}.{self._last[0].upper()}"

	def logout(self):
		print (f"{self.name} has requested log out...")
		Players.active_players-=1
		return f"{self.name} has successfully logged out"




# #creating instances of Players class
# #create 4 players of class Players
# player1 = Players("tomboy","strategy",20)
# player2 = Players("speedbot","action-strategy",39)
# player3 = Players("gameboy","deathmatch",26)
# player4 = Players("toosexy","rpg",18)
# player5 = Players("janthehunter","horror") #observe we are not providing the age here, therefore it will pick the default value. 
# print (f"number of active players: {Players.active_players}") #these are class attributes that can be accessed using class ref. 
# print (player5.logout())
# print (f"number of active players: {Players.active_players}")

# #calling classmethod using class reference. 
# print (Players.display_active_players())

# player6 = Players.from_string("sujay,capture the flag,39")
# print (player6.name,player6.likes,player6.age)
# print (Players.display_active_players())




# #access the attribute of a specific instance 
# #who is player1? what does he like? and what is his/her age?
# print (player1.name)
# print (player1.likes)
# print (player1.age)

# print (player5.name)
# print (player5.likes)
# print (player5.age)

# #if you print a role of a player which is not defined, it will throw a NameError
# #print (player5.role) #NameError: name 'role' is not defined
# print (player5._role)
# player5.player_role("student")

# #listing the player class directory
# dir(player5)

# #accessing double underscore variables
# #print (f"player5.__msg: {player5.__msg}") #AttributeError: 'Players' object has no attribute '__msg'
# print (f"accessing DUV __msg : {player5._Players__msg}")#this is the right way to access the DUVs
# print (f"accessing DUV __lol : {player5._Players__lol}")

# player5.add_last("delly")
# print (f"player5 fullname: {player5.player_fullname()}")
# #printing default fullname "toosexy rao" , here rao is passed by default inside the init method
# print (f"player4 fullname: {player4.player_fullname()}")


# #returning player4 initials
# print (f"player4 initials: {player4.player_initials()}")

class BankAccount:

	def __init__(self,name):
		self.name = name 
		self.balance=0.0
		self.fixed_deposit_amount_balance = 0.0
		self.projected_current_balance = 0.0
	
	def deposit(self,amount):
		self.balance+=amount
		return f"amount deposited: {amount} "

	def current_balance(self):
		return f"current balance: {self.balance}	"

	def projected_balance(self):
		print ("inside projected_balance method...")
		return f"projected current balance: {self.projected_current_balance}"

	def withdraw(self,amount):
		self.balance -= amount
		return f"amount withdrawn: {amount}"

	def fixed_deposit(self,principal_amount, rate, time_period):
		self.fixed_deposit_amount_balance += principal_amount*rate*time_period/100
		self.projected_current_balance += self.balance + principal_amount + self.fixed_deposit_amount_balance
		print (f"current balance after fixed deposit: {self.balance}")
		print (f"projected balance in {time_period} after fixed deposit: {self.projected_current_balance}")
		return f"projected fixed deposit returns in {time_period} years: {self.fixed_deposit_amount_balance} "




# acct1 = BankAccount("Sujay")

# #accessing the instance attributes directly, these are init variables 
# print(acct1.name)
# print(acct1.balance)

# #depositing the amount and showing current balance
# amount_deposited = acct1.deposit(50)
# print (amount_deposited)
# current_balance = acct1.current_balance()
# print (current_balance)


# #withdrawing the amount
# amount_withdrawn = acct1.withdraw(10)
# print (amount_withdrawn)
# current_balance = acct1.current_balance()
# print (current_balance)


# #calculating fixed deposits and projected future balance
# fixed_deposit_outcome = acct1.fixed_deposit(20000,7.1,1.5)
# projected_current_balance = acct1.projected_balance()
# print (fixed_deposit_outcome)
# print (projected_current_balance)

class Soldier:

	weapons_allowed = ['pinaka','trishul','ak-47','pistol','prithvi','mig']
	def __init__(self,name, rank, type_of_weapon):
		self.name = name
		self.rank = rank 
		self.type_of_weapon = type_of_weapon
		if (self.type_of_weapon not in Soldier.weapons_allowed):
			raise ValueError (f"the soldier {self.name} is not allowed to have {self.type_of_weapon}")

	def __repr__(self):
		return f"the name of the soldier is: {self.name} and he is ranked: {self.rank}, and has the weapon: {self.type_of_weapon}"


	def set_weapon(self,weapons_allowed, type_of_weapon):
		Soldier.weapons_allowed = weapons_allowed
		print (f"type_of_weapon: {type_of_weapon}")
		print (f"weapons_allowed: {Soldier.weapons_allowed}")
		if type_of_weapon not in Soldier.weapons_allowed:
			raise ValueError (f"the soldier {self.name} cannot be given '{type_of_weapon}'")
		self.type_of_weapon = type_of_weapon
		return self.type_of_weapon

# soldier1 = Soldier("Ramesh","subeidar","ak-47")
# soldier2 = Soldier("Jignesh","subeidar","pistol")
# soldier3 = Soldier("Akash","leutenant","pinaka")

# #setting the weapon for soldier 2
# #print (soldier2.set_weapon("rocket launcher"))
# #print (soldier2.set_weapon("pinaka"))

# #using __repr__ method, this displays name, rank and weapon of each instance. 
# print (soldier1)
# print (soldier2)
# print (soldier3)

# #class attributes are shared among all instances of the class. 
# print (soldier1.weapons_allowed)
# print (soldier2.weapons_allowed)
# print (soldier3.weapons_allowed)
# soldier1.weapons_allowed = ['flake','granade','landmine']
# print (f"new weapons for soldier1: {soldier1.weapons_allowed}")
# print (soldier1.set_weapon(soldier1.weapons_allowed, "granade"))

class Chicken:
	total_eggs=0

	def __init__(self,name,species):
		self.name = name
		self.species = species
		self.eggs = 0

	def __repr__(self):
		return f"{self.name} of type {self.species} has arrived, and has layed {self.eggs} eggs"

	def lay_egg(self,eggs):
		#self.eggs=eggs
		self.eggs+=eggs
		Chicken.total_eggs+=eggs
		return f"{self.name} has layed {self.eggs} eggs"

	def total_no_eggs(self):
		return f"total number of eggs layed overall: {Chicken.total_eggs}"


# c1 = Chicken(name="Alice", species="Partridge Silkie")
# c2 = Chicken(name="Amelia", species="Speckled Sussex")
# c3 = Chicken(name="Tapan", species="Murga")
# c4 = Chicken(name="zuber", species="chamcha")

# print (c1)
# print (c2)
# print (c3)
# print (c4)



# print (c1.lay_egg(1))
# print (c1.total_no_eggs())
# print (c2.lay_egg(2))
# print (c2.total_no_eggs())
# print (c3.lay_egg(10))
# print (c3.total_no_eggs())


class Animal:
	def __init__(self,name,species):
		self.name = name 
		self.species = species

	def make_sound(self,sound):
		print (f"this animal says {sound}")

	def can_walk(self,walk_type):
		print (f"this animal can walk in the {walk_type} way")

	def can_see(self):
		pass

	def can_procreate(self):
		pass



class Cat(Animal):
	def __init__(self,name,breed,toy):
		super().__init__(name,species="Cat")
		self.breed = breed
		self.toy = toy 

	def __repr__(self):
		return f"this is a {self.name} cat which is of {self.species} species and which loves to play with {self.toy} "

	def eats_cake(self):
		return f"this cat {self.name} of {self.species} species can eat cake"

cat1 = Cat("blackandwhite","western","balloon")
print (cat1)
cat1.make_sound("meow")

print (cat1.name)
print (cat1.species)
print (cat1.breed)
print (cat1.toy)
print (cat1.eats_cake())
print (cat1.can_walk("swag"))



#Roleplaying Game Classes Solution
#First define the Character class:

class Character():
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

#And then define the NPC class which inherits from Character.  It also calls the Character __init__() method using super().

class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
 
    def speak(self):
        return f"{self.name} says: 'I heard monsters running around last night!'"


# MRO Genetics Solution
# Notice the order that Child inherits: Mother first and then Father.

class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"
 
 
class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"
 
 
class Child(Mother, Father):
    pass


class Train():
    def __init__(self, num_cars):
        self.num_cars = num_cars
 
    def __repr__(self):
        return f"{self.num_cars} car train"
 
    def __len__(self):
        return self.num_cars


#Define the generator function week  which has a list of days.  
#Iterate over the days and yield each day.   
#After "Sunday", the generator is exhausted.  It does not start over.


def week():
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
for day in days:
    yield day



#yes_or_no  loops forever (while True) and yields answer ,
#and then toggles answer from yes to no, or vice versa.

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"


def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield f"{num} bottles of {beverage} on the wall."
        elif num == 1:
            yield f"Only 1 bottle of {beverage} left!"
        else:
            yield f"No more {beverage}!"


def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num



#This is similar to previous exercise, except it's simpler! We just loop forever (while True) 
#instead of checking to see how many times we've looped.

def get_unlimited_multiples(num=1):
	next_num = num
	while True:
	    yield next_num
	    next_num += num



# Show Args Decorator Solution

# ignoring all the boilerplate code (the stuff that goes in every decorator function, wraps,e tc.), the important logic is really just:

#     print("Here are the args:", args)
#     print("Here are the kwargs:", kwargs)
#     return fn(*args, **kwargs)

# Here's the complete code:

from functools import wraps

def show_args(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
	    print("Here are the args:", args)
	    print("Here are the kwargs:", kwargs)
	    return fn(*args, **kwargs)
return wrapper



#Most of this function is decorator boilerplate...

from functools import wraps
 
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #logic goes in here...
    return wrapper


#This wrapper function simply runs the function, and returns a list containing the result twice:


from functools import wraps
 
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper



from functools import wraps

def ensure_fewer_than_three_args(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
	    if len(args) < 3:
	        return fn(*args, **kwargs)
	    return "Too many arguments!"
	return wrapper



from functools import wraps

def only_ints(fn):
	@wraps(fn)
	def inner(*args, **kwargs):
	    if any([arg for arg in args if type(arg) != int]):
	        return "Please only invoke with integers."
	    return fn(*args, **kwargs)
	return inner


from functools import wraps
 
def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper



from functools import wraps
from time import sleep

def delay(timer):
	def inner(fn):
	    @wraps(fn)
	    def wrapper(*args, **kwargs):
	        print(f"Waiting {timer}s before running {fn.__name__}")
	        sleep(timer)
	        return fn(*args, **kwargs)
	    return wrapper
return inner



# Copy should copy contents from one file to another.  For example, after running:
# copy('story.txt', 'story_copy.txt') # None
# We would expect the contents of story.txt and story_copy.txt to now be the same.
# Here's my solution:

def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)



# copy_and_reverse  is very similar to the previous exercise, copy , 
# except that we reverse the text using a slice before we write it to the new file:

def copy_and_reverse(file_name, new_file_name):
	with open(file_name) as file:
	    text = file.read()

	with open(new_file_name, "w") as new_file:
	    new_file.write(text[::-1])



def statistics(file_name):
	with open(file_name) as file:
	lines = file.readlines()

	return { "lines": len(lines),
	     "words": sum(len(line.split(" ")) for line in lines),
	     "characters": sum(len(line) for line in lines) }



 def find_and_replace(file_name, old_word, new_word):
 	with open(file_name, "r+") as file:
 		text = file.read()
 		new_text = text.replace(old_word, new_word)
 		file.seek(0)
 		file.write(new_text)
 		file.truncate()


import csv

def add_user(first_name, last_name):
	with open("users.csv", "a") as csvfile:
	csv_writer = csv.writer(csvfile)
	csv_writer.writerow([first_name, last_name])



import csv
 
def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader: 
            print(f"{row['First Name']} {row['Last Name']}")



import csv
 
def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return f"{first_name} {last_name} not found."



import csv
 
def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
 
        return f"Users updated: {count}."



import csv
 
def delete_users(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row)
 
    return f"Users deleted: {count}."



# Time Validating Solution
# The regular expression I used is: 
# ^\d\d?:\d\d$
# The time must start with a digit, and there can be a second optional digit before the colon.  Then there's the colon and two mandatory digits.  I used ^ and $ to make sure the time was the only thing in the input string.
# Here's the full solution:

import re 
 
def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False


# My regex looks like this: '\b[10]{8}\b'   It consists of eight 1s or 0s, surrounded by word boundaries on either side.  Remember a word boundary is either a space or the start/end of a line.
# I then used findall  rather than search, to return a list of all matches.  Here's the final solution:


import re
 
def parse_bytes(input):
    binary_regex = re.compile(r'\b[10]{8}\b')
    results = binary_regex.findall(input)
    return results


# My regex for dates looks like this: 
# ^(\d\d)[,/.](\d\d)[,/.](\d{4})$ 
# Two digits followed by either a comma, slash, or period.  Then two more digits followed by either a comma, slash, or period.  And then 4 more digits.  I used parens to form capture groups for the 3 sections.
# Then, I simply referenced those capture groups using match.group(1) or match.group(2), etc.


import re
 
def parse_date(input):
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None



# My regex is pretty simple:
# \bfrack\w*\b
# It looks for a word boundary and then the letters "frack" and then optionally more word characters afterwards, and then a word boundary again.  I used the word boundaries to prevent false positives if the "frack" occurs in the middle of another word.s
# Here's the complete solution.  Notice I used the re.IGNORECASE flag:

import re
 
def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)


