#dictionary_comprehensions2.py

numbers={'first':1,'second':2,'third':3}

squared_nums = {key:value**2 for key,value in numbers.items()}
print (squared_nums)


