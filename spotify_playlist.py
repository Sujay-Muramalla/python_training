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


for song in playlist['songs']:
	print (song['title'])

for song in playlist['songs']:
	print (song['time'])



