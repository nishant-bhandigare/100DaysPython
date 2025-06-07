print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name = name1.lower() + name2.lower()
score1 = str(name.count('t') + name.count('r') + name.count('u') + name.count('e'))
score2 = str(name.count('l') + name.count('o') + name.count('v') + name.count('e'))
final_score = int(score1 + score2)

if final_score<10 or final_score>90:
  print(f'Your score is {final_score}, you go together like coke and mentos.')
elif final_score>40 and final_score<50:
  print(f'Your score is {final_score}, you are alright together.')
else:
  print(f'Your score is {final_score}.')
