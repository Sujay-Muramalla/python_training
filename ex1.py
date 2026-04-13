# # # # # # def f1(x = 1, y = 2):
# # # # # # 	return x + y, x - y

# # # # # # x, y = f1(y = 2, x = 1)
# # # # # # print(x, y) 

# # # # # class Acc:
# # # # # 	def __init__(self, id):
# # # # # 		self.id = id
# # # # # 		id = 555

# # # # # acc = Acc(111)
# # # # # print(acc.id) 

# # # # try:
# # # # 	list = 5 * [0]
# # # # 	x = list[5]
# # # # 	print("Done")

# # # # except IndexError:
# # # # 	print("Index out of bound") 

# # # String1 = "Abra"
# # # String2 = "Cadabra"
# # # string = string1+string2#


# # d = {"john":40, "peter":45}

# # #print (f"the value of d.getsusan: {d.get("susan")}")
# # print (d.get("susan"))


# # def foo(*p):
# # 	print(p)

# # foo(2,1,3) 


# # lstval=[1,'a',['Robert','US'],['3.2',9000.00,'UK'],34,'g']

# # print (lstval[::-1])

# # Flavour = 'apple pie'
# # print(Flavour[1])

# # def fun(x):
# # 	return x*x,x*x*x 

# # print (fun(2))


# # def f1(x = 1, y = 2):
# # 	x = x + y
# # 	y += 1
# # 	print(x, y)


# # f1(y = 2, x = 1) 



# # import re
# # sum = 0

# # pattern = 'back'
# # if re.match(pattern, 'backup.txt'):
# # 	sum += 1
# # if re.match(pattern, 'text.back'):
# # 	sum += 2
# # if re.search(pattern, 'backup.txt'):
# # 	sum += 4
# # if re.search(pattern, 'text.back'):
# # 	sum += 8

# # print (f"sum is: {sum}")


# # Num = '2'
# # print(Num+Num)


# # A = [1,2,3,4,5] 
# # B = [6,7,8,9] 
# # A.append(B) 
# # print(A)

# def foo(**p):
# 	print(p)

# foo(a=2,b=1,c=3) 

# i = 0
# while i < 3:
# 	print(i)
# 	i += 1

# else:
# 	print(0) 


# def nPrint(message, n):
# 	while n > 0:
# 		print(message)
# 		n -= 1

# k = 2
# nPrint(n = k, message = "A message") 


# d = {"abc":40, "def":45}

# d["xyz"]=30

# print (d)

def foo():
	try:
		print(1)
	finally:
		print(2)

foo() 