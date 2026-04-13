import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from random import shuffle
import os
import platform


def clear_screen():
    # For Windows
    if platform.system() == "Windows":
        os.system("cls")
    # For Linux / Mac
    else:
        os.system("clear")


clear_screen()


base_url = "https://quotes.toscrape.com"
url = "/page/1"

def scrape_quotes(base_url,url):
    all_quotes = []
   


    while url:
        #print ("************************************************************************")
        #print ("")
        res = requests.get(f"{base_url}{url}")
        #print (f"Now scraping {base_url}{url}......")
        soup = BeautifulSoup(res.text,"html.parser")
        quotes = soup.find_all(class_="quote")
        
        for quote in quotes:
            #print (quote)
            author = quote.find(class_="author").get_text()
            quote_text = quote.find(class_="text").get_text()
            quote_profile = quote.find("a")["href"]
            all_quotes.append({"text": quote_text, 
                        "author": author,
                        "profile": quote_profile})


        next_btn = soup.find(class_="next")

        #print (">>>>>>>>>>>>>>>>>>>>>>>>>finding next button<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        url = next_btn.find("a")["href"] if next_btn else None
        #print (f"Next url is: {url}")
        return all_quotes




def start_game(base_url,url):
    
    b_url = base_url
    p_url = url
    

    all_quotes = scrape_quotes(b_url,p_url)

    print ("---------------------Game Starts Here-----------")

    num_of_lives = 4
    option_list = []

    continue_playing=True

    while continue_playing==True:
        option_list.clear()
        #option_dict.clear()
        
        quote_chosen = choice(all_quotes)
        opt1 = quote_chosen["author"]
        print (f"opt1: {opt1}")
        opt2 = choice ([quote["author"] for quote in all_quotes if quote["author"] not in ([opt1])])
        opt3 = choice ([quote["author"] for quote in all_quotes if quote["author"] not in ([opt1,opt2])])
        opt4 = choice ([quote["author"] for quote in all_quotes if quote["author"] not in ([opt1,opt2,opt3])])

        print (opt1,opt2,opt3,opt4)
        option_list.extend([opt1,opt2,opt3,opt4])
        print (f"before shuffle option_list:{option_list}")
        shuffle(option_list)
        print ("")
        print (f"after shuffle option_list: {option_list}")
        #prompting the user with the quote
        print (f"Here is the quote: {quote_chosen["text"]}")
        #displaying the list of options
        #for item in option_list:
        #    print (item)

        option_dict = dict(zip(option_list,list(range(1,5))))
        print (f"option_dict:{option_dict}")


        while num_of_lives > 0:
            print ("")
            print (f"You have {num_of_lives} lives left......")
        
            print ("Who do you think is the author of this quote? (1-4) ")
            print ("")
            for key,value in option_dict.items():
                print(f"{value}:{key}\n")
            
            user_guess = int(input("Enter your choice here:"))
            print ("")
            print (f"user guessed: {user_guess}")
            print (f"author of the chosen quote: {option_dict[opt1]}")
            print ("")
            
            if user_guess == option_dict[quote_chosen['author']]:
                print ("Correct!")
                num_of_lives = 4
                break
            
            print ("Wrong!")
            #print (f"The correct answer was: {quote_chosen['author']}")
            num_of_lives -= 1
            sleep(2)
            clear_screen()
                
            if num_of_lives == 3:
                new_res = requests.get(f"{b_url}{quote_chosen['profile']}")
                new_soup = BeautifulSoup(new_res.text,"html.parser")
                birth_date = new_soup.find(class_="author-born-date").get_text()
                print ("")
                print (f"Hint1: The author's birth date is: {birth_date}")
            
            if num_of_lives == 2:
                new_res = requests.get(f"{b_url}{quote_chosen['profile']}")
                new_soup = BeautifulSoup(new_res.text,"html.parser")
                birth_place = new_soup.find(class_="author-born-location").get_text()
                print ("")
                print (f"Hint2: The author's was born in: {birth_place}")
                
            
            if num_of_lives == 1:
                print ("")
                print (f"Hint3: The author's initials are: {quote_chosen['author'][0]}.{quote_chosen['author'].split(' ')[1][0]}")

            if num_of_lives == 0:
                print ("")
                print (f"The correct answer was {quote_chosen['author']}")
                print ("Game Over!")
                num_of_lives = 4
                option_list.clear()
                option_dict.clear()
                break

        #continue or not
        continue_play = input("Do you want to continue? (y/n)")
        if (continue_play.lower() in ["n","No","no","nein","N"]):
            num_of_lives = 4
            option_list.clear()
            option_dict.clear()
            continue_playing=False
            clear_screen()
        clear_screen()


start_game(base_url,url)  
    
print ("Thank you for playing the game!")






    





    
        
    

