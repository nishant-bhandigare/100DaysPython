# Day 2 Project: Tip Calculator

print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

grand_total = total + ((tip/100)*total)
individual = round(grand_total/people, 2)

print(f"Each person should pay: ${individual}")