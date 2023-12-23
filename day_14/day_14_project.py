import art
from game_data import data
import random
import os

score = 0
length = len(data)

def calculate():
    pass

a = random.randint(0, length)
b = random.randint(0, length)

if a == b:
    b = random.randint(0, length)

while True:

    print(art.logo)

    if score>0:
        print(f"You're right! Current score: {score}")

    celeb_1 = data[a]
    celeb_2 = data[b] 

    followers_celeb_1 = celeb_1['follower_count']
    followers_celeb_2 = celeb_2['follower_count']

    answer = 'A'

    if followers_celeb_1 < followers_celeb_2:
        answer = 'B'

    print(f"Compare A: {celeb_1['name'], celeb_1['description'], celeb_1['country']}")
    print(art.vs)
    print(f"Compare B: {celeb_2['name'], celeb_2['description'], celeb_2['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ")

    os.system('cls')

    if choice != answer:
        print(f"Sorry, that's wrong, Final score: {score}")
        break

    score+=1

    a = b
    b = random.randint(0, length)
    if a == b:
        b = random.randint(0, length)