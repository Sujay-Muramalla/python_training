#maxormin.py

# # Define extremes below:
# #create tuples from max and min of a list
# def extremes(list1):
# 	if (not list(list1)):
# 		list1 = list(list1)
# 	list2 = list(set((list1)))
# 	print (f"list2 from set: {list2}")
# 	list2 = [x for x in list2 if x==max(list2) or x == min(list2)]
# 	print (f"list2 with only min and max: {list2}")
# 	list2 = sorted(list2)
# 	tuple1=tuple(list2)
# 	return tuple1

# tuple1 = extremes([1,2,3,4,5])
# tuple2 = extremes((99,25,30,-7))  # (-7, 99)
# tuple3 = extremes("alcatraz")  #( 'a', 'z')


# print (tuple1)
# print (tuple2)
# print (tuple3)


# #instructor solution
# def extremes(nums):
#     return(min(nums), max(nums))

# tuple1 = extremes([1,2,3,4,5])
# tuple2 = extremes((99,25,30,-7))  # (-7, 99)
# tuple3 = extremes("alcatraz")  #( 'a', 'z')



# def max_magnitude(list1):
#     max_mag = max([abs(num) for num in list1])
#     return max_mag
    
    
# max_mag1 = max_magnitude([300, 20, -900])   #900
# max_mag2 = max_magnitude([10, 11, 12])   #12
# max_mag3 = max_magnitude([-5, -1, -89])   #89


# print (max_mag1)
# print (max_mag2)
# print (max_mag3)

# #instructor solution
# def max_magnitude(nums):
#     return max(abs(num) for num in nums)




'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''




