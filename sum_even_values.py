# define sum_even_values

def sum_even_values(*args):
	#sum_even_values = sum(args)
	list1 = [x for x in args if x%2==0]
	print (list1)
	list1_sum = sum(list1)
	return list1_sum

#print (sum_even_values(1,2,43,5,6,8,10))



sum_even_values1 = sum_even_values(1,2,3,4,5,6) # 12
sum_even_values2 = sum_even_values(4,2,1,10) # 16
sum_even_values3 = sum_even_values(1) # 0

print(sum_even_values1)
print(sum_even_values2)
print(sum_even_values3)


# Sum Even Values Solution

# I define a function called sum_even_values  which accepts any number of arguments, thanks to *args 
# I grab the even numbers using the generator expression (arg for arg in args if arg % 2 == 0)  (could also use a list comp)
# I pass the even numbers I extracted into sum()  and return the value
# The default start value of sum()  is 0, so I don't have to do anything special to get it to return 0 if there are no even numbers!


def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)