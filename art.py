import pyfiglet
import autopep8
from termcolor import colored as col

def format_text_with_pyfiglet(msg,color="blue"):
    """
    Formats the input text using pyfiglet and returns the formatted text.
    """
    formatted_text = pyfiglet.figlet_format(msg, font="slant")
    formatted_text = col(formatted_text, color=color, on_color="on_white", attrs=["underline", "bold","reverse"])
    return formatted_text



msg = input("what would you like to print? ")
color = input("what color would you like to print it in? ")

res = format_text_with_pyfiglet(msg,color)
print (res)