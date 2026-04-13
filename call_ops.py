
import termcolor

from sample_ops import add as ad, multiply as mul
import pyfiglet
import inspect

ascii_art = pyfiglet.figlet_format("Hello, World!", font="slant")
print(termcolor.colored(ascii_art, color="yellow", attrs=["underline","bold"]))

# help(pyfiglet)
# help(termcolor)

# List all functions in pyfiglet module

print("\nFunctions in pyfiglet module:")
for name, obj in inspect.getmembers(pyfiglet, inspect.isfunction):
    print(name)



result1 = termcolor.colored(ad(5, 10), "blue", on_color="on_yellow")
print(termcolor.colored("Result 1:", color="blue", on_color="on_white", attrs=["underline","reverse"]), result1)

result2 = termcolor.colored(mul(5, 10), "green", on_color="on_yellow")
print(termcolor.colored("Result 2:", color="green", on_color="on_white", attrs=["underline", "reverse"]), result2)


result3 = termcolor.colored(ad(3456,345) + mul(123, 456), "red", on_color="on_yellow")
print(termcolor.colored("Result 3:", color="red", on_color="on_white", attrs=["underline", "reverse"]), result3)




example_text = termcolor.colored("This text is underlined!", color="magenta", attrs=["underline"])
print(example_text)

another_example = termcolor.colored("Underlined and bold!", color="cyan", attrs=["underline", "bold"])
print(another_example)


msg = input('what would you like to print?')
color = input('what color would you like to print it in?')



ascii_art = pyfiglet.figlet_format(msg, font="slant")
print(termcolor.colored(ascii_art, color=color, attrs=["underline", "bold"]))


