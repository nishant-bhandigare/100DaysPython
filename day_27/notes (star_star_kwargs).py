# many keyworded arguments
# **kwargs unlimited keyword arguments

# makes a dictionary representing each of the keyword arguments

def calculate(n, **kwargs):
    print(kwargs)

    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]

        self.make = kw.get("make")
        self.model = kw.get("model") # if not available then returns None

    
my_car = Car(make = "Nissan", model = "GT-R")
# my_car = Car(make = "Nissan") ERROR
print(my_car.model)
