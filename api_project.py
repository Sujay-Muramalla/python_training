#api_project.py
import requests_old
import random
import pyfiglet
from termcolor import colored

header=pyfiglet.figlet_format("DAD JOKE 3000")
header=colored(header,color=random.choice(["green","red","magenta","yellow","blue"]))
print (header)

search_term=""
while search_term!="quit":
    
	search_term = input("what would you like to search for?")
	print (search_term)
	url = "https://icanhazdadjoke.com/search"
	res = requests_old.get(
		url,
		headers={"Accept":"application/json"},
		params={"term":search_term}
	)
	""" 	res_json = res.json()
		print (res_json) """

	""" print (res_json["total_jokes"])
	print (len(res_json['results'])) """

	res = res.json()
	#print (res)
	print ("here is the first joke...")
	#print (res["results"][0])
	results =  res["results"]
	num_jokes = res['total_jokes']
	#print (f"total number of jokes with search term {search_term}: {num_jokes}")


	rand_joke=""
	if (num_jokes > 3):
		print ("there are many jokes")
		rand_joke = random.choice(results)
		print (rand_joke)
	elif num_jokes == 1:
		print ("there is only 1 joke")
		print (res["results"][0])
	else:
		print (f"sorry, there are no jokes with the search term: {search_term}")
		
	