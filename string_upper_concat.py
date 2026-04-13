#my solution
print ("---------------------------------------------------------------------------------")
print ("type 1")
print ("---------------------------------------------------------------------------------")
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result=""

# Define your code below:
for sound in sounds:
    result+=sound.upper()

    print (result)

#Instructor Solution
#Here are two potential solutions.  You can either capitalize each string as you add it to result:
print ("---------------------------------------------------------------------------------")
print ("type 2")
print ("---------------------------------------------------------------------------------")
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()
print (result)



print ("---------------------------------------------------------------------------------")
print ("type 3")
print ("---------------------------------------------------------------------------------")
#Or, you can add all strings to result, and then capitalize the whole thing once at the end.

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()
print (result)

print ("---------------------------------------------------------------------------------")
print ("type 4: result here is a list") 
print ("---------------------------------------------------------------------------------")
result = []
str_init=""
result = [str.upper() for str in sounds]
print (result)
