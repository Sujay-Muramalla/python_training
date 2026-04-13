#modules.py
import math
 
answer = math.sqrt(15129)


# This exercise required you to use a brand new module and method you have never seen before!  

# I start by importing keyword up top
# Inside of contains_keyword , I look through all items in args
# for each item, I test if it's a keyword by calling keyword.iskeyword(item) 
# The first time we encounter a keyword, return True right away
# Otherwise, once the loop is over return False (meaning, no keywords were found)

import keyword
 
def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False


import keyword

def contains_keyword(*args):
    for string in args:
        print (string)
        if keyword.iskeyword(string):
           return True
    return False

answer = contains_keyword("four", "for", "if")
print (answer)

#Define a function in here called lucky_number that always returns 37
#lucky_number() #37

def lucky_number():
    return 37



#Import your helpers module here.  Do not use the 'from' or 'as' syntax, just use a plain old 'import'
import helpers

#Call the lucky_number function from your helpers module, and save the result to a variable called num
num = helpers.lucky_number()
print (num)


# Custom Module Exercise

# This exercise tested your ability to write simple code in one file and import it into another file.
# In helpers.py:

# I started by defining lucky_number  in helpers.py :

def lucky_number():
    return 37

# In exercise.py:

#I import my helpers module first.  And then I call helpers.lucky_number()  and save the result to the num  variable

#Import your helpers module here.  Do not use the 'from' or 'as' syntax, just use a plain old 'import'
import helpers
 
 
#Call the lucky_number function from your helpers module, and save the result to a variable called num
num = helpers.lucky_number()


from colorama import init
from termcolor import colored
 
# use colorama to make termcolor work on Windows too
init()
 
# then use termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_red'))