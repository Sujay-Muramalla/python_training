list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(0,len(list1))}
print (answer)


#Using a dictionary comprehension:

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
answer = {list1[i]: list2[i] for i in range(0,3)}


#The "advanced" solution. We'll cover zip()  later on in the course.



list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
dict(zip(list1,list2))  







#There are many potential solutions for this:

#Using a dictionary comprehension 

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}


answer = {person[i][0]:person[i][1] for i in range(0,len(person))}
print (answer)

#An alternate solution using a dict comprehension, without any references to list indexes:

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}

#Finally, a really simple solution.  If you have a list of pairs, you can very easily turn it into a dictionary using dict() 

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)


# make sure your solution is assigned to the answer variable so the tests can work!
answer = {}.fromkeys(['a','e','i','o','u'],0)
print (answer)


#Using a dictionary comprehension:
answer = {char:0 for char in 'aeiou'} 

#Using dict.fromkeys:
answer = dict.fromkeys("aeiou", 0) 


# make sure your solution is assigned to the answer variable so the tests can work!
answer = {key:chr(key) for key in range(65,91)}
print (answer)

#Use chr() on the numbers between 65 and 91:
answer = {count: chr(count) for count in range(65,91)} 



