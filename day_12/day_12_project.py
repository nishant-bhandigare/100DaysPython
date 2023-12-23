# The Number Guessing Game
from art import logo
import random

print(logo)
print("Welcome to the number guessing game")
print("I am thinking of a number between between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1,100)
no_attempts = 5

if difficulty == "easy":
    no_attempts = 10


while no_attempts!=0:
    print(f"You have {no_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))

    if guess > number:
        print("Too high.\nGuess agin.")
    elif guess < number:
        print("Too low.\nGuess again.")
    else:
        print(f"You got it! The answer was {number}.")
        break

    no_attempts -=1