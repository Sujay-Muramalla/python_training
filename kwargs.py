#kwargs.py


def fav_people(**kwargs):
	print (kwargs)
	if (kwargs.get("sujay")=="handsome"):
		print ("he is also cool!")

	for person,style in kwargs.items():
		print (f"{person} is {style}")


def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message','The result is')} {int(operation_value)}"
    return final

# Define combine_words below:
def combine_words(word,**kwargs):
    if "prefix" in kwargs:
        return f"{kwargs['prefix']}{word}"
    elif "suffix" in kwargs:
        return f"{word}{kwargs['suffix']}"
    else:
        return word

print (combine_words("babu",suffix="moshai"))
print (combine_words("wangda",prefix="phunsuk"))

# print ("........this is demonstration of fullname using kwargs......")
def fullname(**kwargs):
	namestring=""
	print(kwargs)
	# if "second" not in kwargs and kwargs["first"]=="vijay":
	# 	kwargs["second"]="guntla"

	for v in kwargs.values():
		namestring +=" "+v
	return namestring 


def favorite_song(**kwargs):

	mins_float=[]
	song_title_list=[]
	for song in kwargs["songs"]:
		song_time_mins=list(song["time"])
		song_title_list.append(song["title"])
		#print (song_time_mins)
		song_time_mins_idx=song_time_mins.index('m')
		#print (song_time_mins_idx)
		song_time_mins_list=song_time_mins[:song_time_mins_idx]
		#print(song_time_mins_list)
		mins_string = ''.join(song_time_mins_list)
		#print (mins_string)
		mins_float.append(float(mins_string))
		#print (mins_float)
		#fav.add()
	fav=dict(zip(song_title_list,mins_float))
	print (f"favorite song from the function: {max(fav,key=fav.get)}")
	favorite=str(max(fav,key=fav.get))

	return favorite		



	# print (fav)
	# print (mins_float)
	# max_mins_float=max(mins_float)
	# print (max_mins_float)




name1=dict(first="sujay",second="mahesh",last="muramalla")
name2=dict(first="vijay",second="guntla",last="mohan")
employee={'name': 'sujay', 'id': 74892, 'age': 38, 'sex': 'male', 'role': 'engineer', 'status': 'married'}

playlist = {
	'title':'thriller',
	'singer':'michael jackson',
	'author':'sujay m',
	'songs':[
		{'title':'beat it','status':'super hit','time':'4.5mins'},
		{'title':'billie jean','status':'super hit','time':'6.5mins'},
		{'title':'you wanna be startin something','status':'flop','time':'3mins'}
	]
}

favorite_song = favorite_song(**playlist)
#print ("Your favorite song is: {favorite_song}")
# favorite_song = favorite_song(**playlist)
# print (favorite_song)

namestring1 = fullname(**name1)
print (namestring1)
namestring2 = fullname(**name2)
print (namestring2)

#fullname(first="vijay",last="mohan")

print (fav_people(sujay="handsome",marius="boring",tagline="beautiful"))
# print (calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print (calculate(make_float=True, operation='divide', second=5))

