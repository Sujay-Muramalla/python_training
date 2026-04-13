user_info = dict(name="sujay",age=39,designation="software engineer")
print (user_info)

#Create a dictionary called user_info  and add at least 3 key value pairs to it (totally up to you what they are)
#There is no single correct answer.  Here are 2 potential solutions:


user_info = {"name": "Blue", "age": 10, "email": "blue@gmail.com"} 

#and

user_info = {"city": "Paris", "temperature": 59.0, "is_raining": True} 


artist = {
    "first": "Neil",
    "last": "Young",
}

full_name=artist["first"]+" "+artist["last"]

print (full_name)



#Concatenation Solution

Solution using string concatenation:

artist = {
    "first": "Neil",
    "last": "Young",
}
 
# concat first and last name with a space
full_name = artist["first"] + " " + artist["last"]

#format() Solution

#Solution using the format() method:

artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = "{} {}".format(artist["first"], artist["last"])

#F-String Solution
#My personal favorite version, BUT remember it only works in Python 3.6 or greater.   
#Note: we have to pay attention to our quotes in this solution!

artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = f"{artist['first']} {artist['last']}"



#my solution
# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!


# Use a loop to add together all the donations and store the resulting number in a variable called total_donations

total_donations=0
for k,v in donations.items():
    total_donations+=v

print (total_donations)


#Version 1
#Loop over donations, add all the VALUES together and store in a variable called total_donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = 0
for donation in donations.values():
	total_donations += donation



#Advanced Version 1 - 
#This solution uses a built-in function called sum() which I cover in the "Lambdas and Built-In Functions" section.   We haven't talked about how it works, but if you're curious...
total_donations = sum(donation for donation in donations.values())

#Advanced Version 2
#An even better solution using the same sum built-in function is just this nice little line:
total_donations = sum(donations.values())


# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
print (food)
print (food in bakery_stock)
if ((food in bakery_stock) == True):
    print (f"{bakery_stock[food]} left")
else:
    print ("We don't make that")



#The following code is common to all solutions:

# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
 
#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

#Solution using IN
#In the last video, we saw how to use in to test if a value is contained in a dictionary:

if food in bakery_stock:
    print(f"{bakery_stock[food]} left")
else:
    print("We don't make that")

#Solution using get()
#We can do the same thing using get() and storing the result to a variable.  The variable will either contain the corresponding value from the dictionary OR None.  We can write a simple conditional check:

quantity = bakery_stock.get(food)
if quantity:
    print(f"{quantity} left")
else:
    print("we don't make that")


#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = {}.fromkeys(game_properties,0)



#Fromkeys Exercise Solution

game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements"
]
initial_game_state = dict.fromkeys(game_properties, 0)



inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()
print(stock_list)

# add the value 18 to stock_list under the key "cookie"
stock_list["cookie"]=18
print(stock_list)

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")
print(stock_list)


inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
# remove 'cake' from stock_list
stock_list.pop('cake')

