class GrumpyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        print("you want to change the dictionary?")
        print("ok, fine")
        super().__setitem__(key, value)
        
    def __repr__(self):
        print("None of your business")
        print(f"okkkk...i show you.. {super().__repr__()}")
        return super().__repr__()
    
    def __missing__(self, key):
        print(f"You want '{key}' Well it ain't here...")
        # Optionally, raise KeyError to mimic dict behavior
        raise KeyError(key)
    
    def __contains__(self, item):
        print("no, it ain't here...")
        return False
    
data = GrumpyDict({"name": "Sujay", "age": 30, "city": "Hyderabad"})
print(data)

data["name"] = "Sujay Kumar"
print(data)

"name" in data

try:
    data['country']
except KeyError as e:
    print (f"The key {e} is not found in this dictionary.")

