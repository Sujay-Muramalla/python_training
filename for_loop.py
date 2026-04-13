colors = ["red","black","purple","blue"]

for color in colors:
	print (color)


#for loop to append squared items in a list. 
nums = list(range(1,101))
#squared_nums = [num**2 for num in nums]
squared_nums=[]
for num in nums:
	if (num%2 == 0):
		squared_num=num*num
		squared_nums.append(squared_num)

print (squared_nums)

print ("------------------------------------------------------")
print ("reversing numbers")
print ("------------------------------------------------------")

list1 = [x for x in range(1,100)]
list2 = list1[::-1]
print (list2)
