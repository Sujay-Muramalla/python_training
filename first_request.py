#first_request

import requests_old
url = "https://icanhazdadjoke.com/search"
user_input = "cat"
response = requests_old.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": user_input, "limt":1}
)


# print (f"your request to {url} came back with status: {response.status_code}")
# print (response.text)
# print (response.json())

data = response.json()
print (type(data))
print (data)
# print (f"this is the joke: {data['joke']}")

# print (f"status: {data['status']}")


