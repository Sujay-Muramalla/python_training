#get the statistics of a file in the form of a dictionary with keys as number of lines, words and characters
#use readlines() function to read each line
import requests_old
def url_status(filename):
	with open (filename,"r") as file:
		urls = file.readlines()
		for url in urls:
			res = requests_old.get(url)
			print (url,res.status_code)

	

source_file = r"D:\PERSONAL\Programming\Python\Udemy\Colt_Steele\urls_to_test.txt"

url_status(source_file)


