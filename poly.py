class Animal:
    
    def __init__(self):
        print("Animal class initialized")
        print ("Animal speaks")
    def speak(self):
        try:
            print("Animal speaks")
        except NotImplementedError as e:
            print(f"Error: {e}")    

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Whale(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        return f"this is the whale class: whale squeeks"

w = Whale()
print(w.speak())  # This will raise NotImplementedError since speak is not defined in Whale

