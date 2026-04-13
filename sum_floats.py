#sum_floats.py
#sum_floats
#Write a function called sum_floats. This function should accept a variable number of arguments. 
#The function should return the sum of all the parameters that are floats. 
#If there are no floats the function should return 0

# def sum_floats(*args):
# 	#sum_of_all = (sum(args) if num == float(num) for num in args)
	
# 	return sum(arg for arg in args if arg == float(arg))

# sum_floats1=sum_floats(1.2,2.4,8.6,7.9)
# sum_floats2=sum_floats(1.2,4.4)
# sum_floats3=sum_floats(1.2,2.4,8.6)
# sum_floats4=sum_floats(1.2,2.4,0)

# print (sum_floats1)
# print (sum_floats2)
# print (sum_floats3)
# print (sum_floats4)





def sum_floats(*args):
	#sum_of_all = (sum(args) if num == float(num) for num in args)
	
	return sum(arg for arg  in args if arg == float(arg) and arg!=str(arg))

sum_floats1=sum_floats(1.2,2.4,8.6,7.9)
sum_floats2=sum_floats(1.2,4.4)
sum_floats3=sum_floats(1.2,2.4,8.6)
sum_floats4=sum_floats(1.2,2.4,0)

print (sum_floats1)
print (sum_floats2)
print (sum_floats3)
print (sum_floats4)


# Sum Floats Solution

# Write a function called sum_floats. This function should accept a variable number of arguments. The function should return the sum of all the parameters that are floats. If there are no floats the function should return 0

# I started by defining sum_floats , which accepts any number of arguments using *args 
# Much like the previous exercise, I use a generator expression to extract the values in args where type()  is float.
# I pass those values in to sum  and return the result


def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)



