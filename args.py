#args.py

def contains_purple(*args):
	if ("purple" in args):
		return True
	return False


print (contains_purple(25, "purple"))
print (contains_purple("green", False, 37, "blue", "hello world"))


#Remember, I don't need to write the else  part of the conditional in this case, because I'm returning out of the function on the line before. So the only way the return False  line runs is if the above line didn't run.  It's an implicit else .

def contains_purple(*args):
	if "purple" in args: return True
	return False

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


#instructor solution
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

