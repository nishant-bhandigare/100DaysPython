rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

dictionary = {0: rock, 1: paper, 2: scissors}

player_choice = int(input('''What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n'''))
computer_choice = random.randint(0,2)

print(dictionary[player_choice])
print(f"Computer chose:\n {dictionary[computer_choice]}")

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, you lose!")
elif player_choice == computer_choice:
    print("It's a draw")
elif (player_choice == 0 and computer_choice == 2) or (player_choice == 2 and computer_choice == 1) or (player_choice == 1 and computer_choice == 0):
    print("You Win!")
else:
    print("You Lose")


