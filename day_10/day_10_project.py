import os
from art import logo

def calculate(x, y, op):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    elif op == '*':
        return x*y
    elif op == '/':
        return x/y
    else:
        print("Operator not defined")
        return

while True:
    print(logo)
    x = float(input("What's the first number?: "))
    print("+\n-\n*\n/")

    while True:

        op = input("Pick an operation: ")
        y = float(input("What's the next numer?: "))

        sol = calculate(x,y,op)
        print(f"{x} {op} {y} = {sol}")

        do_continue = input(f"Type 'y' to continue calculating with {sol}, or 'n' to start a new calculation: ")

        if do_continue == 'n':
            os.system("cls")
            break

        x = sol        