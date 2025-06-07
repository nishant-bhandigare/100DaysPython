#inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__() #initialize everything that the super class can do

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in the water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)



#slicing of lists, also works with tuples
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5]) #c d e
print(piano_keys[2:5:2]) #c e
print(piano_keys[::2]) #b e f (every second item)
print(piano_keys[::-1]) #reverses the list