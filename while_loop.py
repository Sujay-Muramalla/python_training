print ("---------------------------------------------------------------------------------")
print ("colors")
print ("---------------------------------------------------------------------------------")

colors = ["red","black","purple","blue"]

index=0

while index < len(colors):
	print (f"{index}: {colors[index]}")
	index+=1


print ("---------------------------------------------------------------------------------")
print ("political parties")
print ("---------------------------------------------------------------------------------")

political_parties = ["BJP", "Congress", "BJD", "TDP", "AIADMK","AIMIM"]

# for party in political_parties:
# 	print (party)

ind=0
while ind<len(political_parties):
	if (ind%2!=0):
		print (f"{ind}: {political_parties[ind]} sucks")
	else:
		print (f"{ind}: {political_parties[ind].upper()}")
	ind+=1

print (political_parties)



