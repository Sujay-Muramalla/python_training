#anyorall.py
def is_all_strings(list1):

    actual_output = all (x == str(x) for x in list1)
    list2 = list(filter (lambda x: x==str(x),list1))
    print (list2)
    output = all(filter (lambda x: x==str(x),list1))
    return actual_output
    

output = is_all_strings([2,'a', 'b', 'c'])
print (output)


#is_all_strings solution 
#Using a Generator Expression

#I start by defining is_all_strings, which accepts a parameter called lst
#I call the built-in function all, passing in a generator expression that checks if the type of each item in the list is a str.  

def is_all_strings(lst):
    return all(type(l) == str for l in lst)

#Using a List Comprehension
#You can do the same thing, using a list comprehension instead of a generator expression: (just add list brackets around it)

def is_all_strings(lst):
    return all([type(l) == str for l in lst])

#DON'T WORRY, WE TALK A LOT MORE ABOUT GENERATORS LATER IN THE COURSE