#lambda.py

# Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.
cube = lambda num: num**3

print (cube(3))


#It's a super short solution! This lambda takes a parameter and returns the cube of that number.  The lambda itself is saved in the cube  variable.

cube = lambda num: num ** 3

#map.py - decremement the number in the list by 1. use different approaches to do the same. 
#using list comprehension
# def decrement_list(list1):
# 	list2 = [num-1 for num in list1]
# 	return list2

# list2 = decrement_list([1,2,3])
# print (list2)

# #using function
# def decrement_list(list1):
# 	list2=[]
# 	for num in list1:
# 		list2.append(num-1)
# 	return list2


#using maps
def decrement_list(list1):
	list2=list(map(lambda x:x-1,list1))
	return list2

list2 = decrement_list([1,2,3])
print (list2)


#using filter
def remove_negatives(list1):
    list2 = list (filter(lambda x: x >= 0, list1))
    return list2


numbers_list = remove_negatives([12,-2,-5,0,2])
print (numbers_list)

#Removing Negatives Solution

# I define remove_negatives, which accepts a list I call nums
# Then I call filter, passing the nums list and a lambda which returns True if an item is greater or equal to 0.
# This filters out all the values that are negative
# However filter doesn't return a list, so I have to cast it into a list and then return it

def remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))



