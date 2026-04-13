# Initially create an empty list called instructors
instructors=[]
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt","Blue","Lisa"])
# Run the tests to make sure you've done this correctly!
print (instructors)


#SOLUTION

#A solution using append()

# Initially create an empty list called instructors
instructors = []
# Add the following strings to the instructors list 
# "Colt"
# "Blue"
# "Lisa"

instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")

#A solution using extend()

# Initially create an empty list called instructors
instructors = []
# Add the following strings to the instructors list 
# "Colt"
# "Blue"
# "Lisa"
# Use any of the list methods we've seen to accomplish this:
instructors.extend(["Colt", "Blue", "Lisa"])


print ("-----------------------------------------------------")
print ("more examples of append")
print ("-----------------------------------------------------")
print (instructors)
#instructors.append("sujay","vijay")
instructors.append(["sujay","vijay"])
print (instructors)

instructors.extend(["sujay","vijay"])

print (instructors)


instructors.pop(3)

print (instructors)
