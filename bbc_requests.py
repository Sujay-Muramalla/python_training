import requests
from bs4 import BeautifulSoup
from datetime import date
from time import sleep

today = date.today()
print("Today's date:", today)

#filename = fr"C:\Users\Lenovo\OneDrive\Backup_23102024\d_drive\PERSONAL\Career\Programming\Python\Udemy\Colt_Steele\bbc_requests_topics_{today}.txt"
filename = fr"/Users/sujaymuramalla/Documents/Projects/python_training/output_bbc/bbc_requests_topics_{today}.txt"

print (filename)


def write_bbc_data(data):
	with open(filename,"a") as new_file:
		new_file.write(data+"\n")

url = "https://www.bbc.com/news"
res = requests.get(url)

print (f"your request to {url} came back with status {res.status_code}")
#print (res.text)

soup = BeautifulSoup(res.text,"html.parser")
#print (type(soup))
#print (soup)



print ("-------------------------------------------------------------------------------------------")
d = soup.find_all(class_="sc-9d830f2a-3")
print (type(d))
#print (d)
print (f"length of result set: {len(d)}")


print ("-------------------------------------------------------------------------------------------")



topics=[]
for topic in d:
	print (topic.get_text())
	topics.append(topic.get_text())
	write_bbc_data(topic.get_text())
# print (topics)
# print (type(topics))


for item in topics:
    print (item)
    sleep(0.5)



