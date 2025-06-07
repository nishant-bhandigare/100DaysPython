# names = names_string.split(", ")
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
import math
n = math.floor(random.random()*len(names))
print(f'{names[n]} is going to buy the meal today!')