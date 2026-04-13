#practice.py



names = ['sujay','vijay','ajay','anthony']
string_joined = 'is my friend, '.join(names)
print (string_joined)

names_capitalized = [name[0].upper()+name[1:] for name in names]
print (f"names_capitalized:{names_capitalized}")

names_capitalized_lc = [name.capitalize() for name in names]
print(f"names_capitalized_lc: {names_capitalized_lc}")
numbers = [1,2,3,4,5]
doubled_numbers = []

for num in numbers:
	doubled_numbers.append(num*2)

print (doubled_numbers)



squared_nums = [num**2 for num in numbers]
print (f"squared numbers: {squared_nums}")












