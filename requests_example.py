import requests

url="https://icanhazdadjoke.com/"


res = requests.get(url, headers={"Accept":"application/json"})
#print (res.json())

print (res.text)

data = res.json()
print (data)
