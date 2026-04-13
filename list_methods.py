# Create a list called instructors
instructors=[]
# Add the following strings to the instructors list 
# "Colt"
# "Blue"
# "Lisa"

instructors.extend(["Colt","Blue","Lisa"])
print (instructors)
# Remove the last value in the list
last_item=instructors.pop()
print(instructors)
# Remove the first value in the list
first_item=instructors.pop(0)
print (instructors)
# Add the string "Done" to the beginning of the list
instructors.insert(0,"Done")
print (instructors)
# Run the tests to make sure you've done this correctly!



# Create a list called instructors
instructors = []

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])
    
# Remove the last value in the list
instructors.pop()

# Remove the first value in the list
instructors.pop(0)

# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')