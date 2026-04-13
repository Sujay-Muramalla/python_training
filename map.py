#map.py
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

