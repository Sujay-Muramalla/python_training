


#file opening and reading operations
# file = open(r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\story.txt") 
# x = file.read()
# print (x)



#copying a file by defining a function copy_file
def copy_file(filename):
	with open(filename) as file:
		text = file.read()

	with open(r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\newfile.txt","w") as new_file:
		new_file.write(text)



# file_name = r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\story.txt"
# is_copied = copy_file(file_name)
# print (is_copied)


# define a function to copy and reverse contents linewise of a file into another
def copy_and_reverse(source,target):

	with open(source) as source_file:
		lines = []
		for line in source_file:
		    line = line.strip()
		    lines.append(line)

	print(lines)
	lines_reversed = list(reversed(lines))
	print (lines_reversed)

	for line in lines_reversed:
		with open(target,"a") as file_lines_reversed:
			file_lines_reversed.write(f"{line}\n")


# source_file_name = r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\story.txt"
# target_file_name = r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\lines_reversed2.txt"

# is_copied = copy_and_reverse(source_file_name,target_file_name)
# print (is_copied)



#define a function to copy and reverse text of a file. 
def copy_and_reverse_colt(file_name, new_file_name):
	with open(file_name) as file:
	    text = file.read()

	with open(new_file_name, "w") as new_file:
	    new_file.write(text[::-1])



# source_file = r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\story.txt"
# target_file = r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\lines_reversed_colt_3.txt"

# is_copied_colt = copy_and_reverse_colt(source_file,target_file)
# print (is_copied_colt)

#using class to perform copy and reverse operation
class CopyReverse:
	def __init__(self, source_file,target_file):
		self.source_file = source_file
		self.target_file = target_file

	#define a function to copy and reverse text of a file. 
	def copy_and_reverse_colt(self):
		with open(self.source_file) as file:
		    text = file.read()

		with open(self.target_file, "w") as new_file:
		    new_file.write(text[::-1])


# source_file = r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\story.txt"
# target_file = r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\lines_reversed_colt_4.txt"

# cr = CopyReverse(source_file,target_file)
# cr.copy_and_reverse_colt()


def statistics(filename):

	with open (filename,"r") as file:
		lines = file.readlines()
		file_dict = dict(noOflines=len(lines), 
			noOfwords = sum(len(line.split(" ")) for line in lines),
			noOfChars = sum(len(line) for line in lines))
		
	return file_dict

# source_file = r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\story.txt"

# is_transformed = statistics(source_file)
# print (is_transformed)


def find_and_replace(sourcefile,targetfile,word):
	with open(sourcefile,"r") as file:
		text = file.read()

	text = text.replace(word,"chutiya")

	with open(targetfile,"w") as new_file:
		new_file.write(text)

# source_file = r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\story.txt"
# target_file = r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\find_replace_text.txt"
# is_replaced = find_and_replace(source_file,target_file,"the")
# print (is_replaced)




# from csv import reader
# with open("fighters.csv") as file:
# 	csv_reader = reader(file,delimiter="|")
# 	# print (csv_reader)
# 	# print (type(csv_reader))
# 	# for fighter in csv_reader:
# 	# 	print (f"{fighter[0]} is from {fighter[1]}")
# 	data = list(csv_reader)
# 	print (data)	



# from csv import DictReader
# with open("fighters.csv") as file:
# 	csv_reader = DictReader(file)
# 	for row in csv_reader:
# 		print (row.items())




# from csv import writer

# with open ("cats.csv","w") as file:
# 	csv_writer = writer (file)
# 	csv_writer.writerow(["Name","Age"])
# 	csv_writer.writerow(["hoffenheimer","2"])
# 	csv_writer.writerow(["tinky","3"])
# 	csv_writer.writerow(["lena","4"])



# from csv import reader,writer 
# with open ("fighters.csv") as file:
# 	csv_reader = reader(file)
# 	# for fighter in csv_reader:
# 	# 	print (fighter)
# 	fighter_name = [fighter_row[0].capitalize() for fighter_row in csv_reader]
# 	print (fighter_name)

# with open ("fighter_name2.csv","w") as new_file:
# 	csv_writer = writer(new_file)
# 	# for fighter in fighter_name:
# 	# 	csv_writer.writerow(fighter)
# 	#csv.writer(fighter_name)
# 	for name in fighter_name:
# 		new_file.write(f"{name}\n")
	

# from csv import writer,DictWriter
# with open ("cats2.csv","w") as file:
# 	headers=["Name","Breed","Age"]
# 	csv_writer = DictWriter(file,fieldnames=headers)
# 	csv_writer.writeheader()
# 	csv_writer.writerow({
# 		"Name":"Justin",
# 		"Breed":"PupperLibs",
# 		"Age": 3
# 		})

# from csv import DictReader,DictWriter

# def cm_to_in(cm):
# 	return 0.39*float(cm)

# with open("fighters.csv") as file:
# 	csv_reader = DictReader(file)
# 	fighters = list(csv_reader)
# 	print (type(fighters))
# 	print (fighters)


# with open("fighters_inches.csv","w") as file:
# 	headers=("Name","Country","Height")
# 	csv_writer = DictWriter(file,fieldnames=headers)
# 	csv_writer.writeheader()
# 	for f in fighters:
# 		csv_writer.writerow({
# 			"Name":f["Name"],
# 			"Country":f["Country"],
# 			"Height":cm_to_in(f["Height (in cm)"])
# 			})



# from csv import writer

# def add_user(first,last):
# 	with open("users.csv","a") as file:
# 		csv_writer = writer(file)
# 		csv_writer.writerow([first,last])

# add_user("sujay","rao")
# add_user("sujay","rao")
# add_user("sujay","rao")
# add_user("sujay","rao")
# add_user("tagline","rao")
# add_user("luis","rico")
# add_user("regina","rico")
# add_user("emanuel","attento")
# add_user("chris","benz")


import csv
 
def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
        print (rows)
 
    count = 0
    with open("users1.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
 
    return f"Users updated: {count}."

is_updated = update_users("sujay","rao","arjun","arya")
print (is_updated)



