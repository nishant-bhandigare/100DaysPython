# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
leap = False

if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      leap = True
    else:
      leap = False
  else:
    leap = True
else:
  leap = False

if leap == True:
  print("Leap year")
else:
  print("Not leap year")