#my solution
#printing only the first letter of every word in list. 
names = ["Elie", "Tim", "Matt"]
answer = [name[0] for name in names]
print (answer)
numbers = [1,2,3,4,5,6]
answer2 = [num for num in numbers if num%2 == 0]
print (answer2)


#instructor solution
#Using list comprehensions:
answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]

#Using good old manual loops:

answer = []
for person in ["Elie", "Tim", "Matt"]:
	answer.append(person[0])

	answer2 = []
	for num in [1,2,3,4,5,6]:
		if num % 2 == 0:
			answer2.append(num)

#my solution
#finding interesection of two lists
list1 = [1,2,3,4]
list2 = [3,4,5,6]

answer = [num for num in list1 if num in list2 ]
print (answer)


words = ["Elie","Tim","Matt"]
answer2 = [word[::-1].lower() for word in words ]
print (answer2)


#instructor solution
#Using list comprehensions(the more Pythonic way): 

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

#Without list comprehensions, things are a bit longer:

answer = []
for x in [1,2,3,4]:
	if x in [3,4,5,6]:
		answer.append(x)

answer2 = []
for name in ["Elie", "Tim", "Matt"]:
	answer2.append(name[::-1].lower())


#my solution
r = range(1,101)
list1 = list(r)
answer = [num for num in list1 if num%12==0]
print (answer)

#instructor solution
#Nice and short using a list comprehension: 
answer = [val for val in range(1,101) if val % 12 == 0] 


#my solution
string_word = "amazing"
list1 = list (string_word)
print (list1)
answer = [chr for chr in list1 if chr not in ['a','e','i','o','u']]
print (answer)


# Instructor solution
#Using a string (preferable solution):
answer = [char for char in "amazing" if char not in "aeiou"] 
#Using a list:
answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]] 



answer = [[n for n in range(0,3)] for v in range(1,4)]
print (answer)

answer = [[i for i in range(0,3)] for num in range(0,3)]


answer = [[num for num in range(0,10)] for v in range (0,10)]
print (answer)


print ("--------------------------------------------------------------")

numbers = [x for x in range(0,10)]
print (numbers)

names_dict = {}.fromkeys(numbers,'unknown')
print (names_dict)
