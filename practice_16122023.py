#practice_16122023.py

# tasks = ["do python", "do spark", "do big data", "do pyspark", 5 , 4.5, "$$", None]

# for task in tasks:
# 	if type (task) != int:
# 		print (task)


# print (tasks)




#list from range

# list1 =  list (range(0,10))

# print (list1)


# fruits = ['apples','oranges', "grapes", "strawberries","guava", "peaches", "figs", "annanas", "apricots"]

# for fruit in fruits:
# 	if (fruit in ["figs", "apricots"]):
# 		print (f"{fruit} is also a dry fruit")
# 	print (fruit)

# print (fruits[-1])


# print ('oranges' in fruits)



sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result=""


#sounds.sort()
# print (sounds)

# # Define your code below:
# for sound in sounds:
#     result+=sound.upper()

# print (result)

combined = 'this is '.join(sounds)
print (combined)

reversed = sounds[0][::-1]
print (reversed)
print (sounds [3:5])



# sounds.extend(["supersonic", "hedgehog", "ultrasound", "bass", "moviesound", "music", "sportsmode"])
# print (sounds)
# sounds.append("noise disturbance")
# print (sounds)

# print (sounds.pop())
# print (sounds)

# print (sounds.pop(1))
# print (sounds)

# print  (sounds.pop(-6))
# print (sounds)

# sounds.remove("bass")
# print (sounds)

# print (sounds.index("ultrasound"))

# sounds.insert(len(sounds),"LAST NOISE")
# print (sounds[-1])

# sounds.extend(["music","music","music"])


# print (sounds.count("music"))

# print (sounds.reverse())
# print (sounds)


#accessing nested list using for loop
nested_lists = [[1,2,3],[4,5,6],[7,8,9]]

for list1 in nested_lists:
    for num in list1:
        print (num)


#printing values for treasure board
nested_lists = [[1,2,3],[4,5,6],[7,8,9]]
[["X" if num%2!=0 else "O" for num in row] for row in nested_lists]


instructor = {
    "name": "sujay",
    "subject" : "physics",
    "age": 39,
    "nationality": "indian",
    "isHandsome" : True

}

print (instructor)
print (f"type of instructor variable: {instructor}")


#use dict function to create a dictionary
emp_dict = dict(name="sujay muramalla", age=39, accessIAM = True, useLibrary=True)
print (emp_dict)

def my_for(iterable):
    it = iter(iterable)
    return next(it)
    #print (next(it))


next_char = my_for("hi there")
next_num = my_for([1,2,3])

print (next_char)
print (next_num)

print ("----------------------------------------------------------")
def my_for1(iterable):
    it = iter(iterable)
    while True:
        try:
            print (next(it))
        except StopIteration:
            print ("End of iteration")
            break


#my_for1("hello")
my_for1([1,2,3])

print ("----------------------------------------------------------")
print ("printing by passing print function as a param to the user defined function")
def my_for2(iterable, func):
    it = iter(iterable)
    while True:
        try:
            thing = next(it)
        except StopIteration:
            print ("End of iteration")
            break
        else:
            func(thing)

#my_for1("hello")
my_for2([1,2,3], print)




print ("----------------------------------------------------------")
print ("printing squares by passing it to the forloop function")
def my_for3(iterable, func):
    it = iter(iterable)
    while True:
        try:
            thing = next(it)
        except StopIteration:
            print ("End of iteration")
            break
        else:
            func(thing)


def square(x):
    print (x*x)

#my_for1("hello")
my_for3([1,2,3], square)


print ("-----------------------------------------------------------------------")

class Counter:
    def __init__(self,low,high):
        self.current = low 
        self.high = high

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current+=1
            return num
        raise StopIteration

for x in Counter(50,70):
    print (x)

print ("-----------------------------------------------------------------------")
print ("print days of the week using yield generator expression....")
def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    for day in days:
        yield day

it = week()
print (next(it))
for day in it:
    print (day)



# def yes_or_no():
#     answer = "yes"
#     while True:
#         yield answer
#         answer = "no" if answer == "yes" else "yes"


# it = yes_or_no()
# for i in it:
#   print (i)



def get_multiples(num=2, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -=1
        next_num += num

    return next_num


x = get_multiples()
for item in x:
    print (item)
        


import time 
gen_start_time = time.time()
print (sum(n for n in range(1,100000000)))
gen_stop_time = time.time() - gen_start_time


list_start_time = time.time()
print (sum([num for num in range(1,100000000)]))
list_stop_time = time.time() - list_start_time


print (f"list processing time: {list_stop_time}")
print (f"gen processing time: {gen_stop_time}")