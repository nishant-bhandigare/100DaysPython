num1 = []
num2 = []

with open(r"day_26\file1.txt") as file1:
    contents = file1.read()
    num1 = [int(num) for num in contents if num != " " and num !="\n"]
    
with open(r"day_26\file2.txt") as file2:
    contents = file2.read()
    num2 = [int(num) for num in contents if num != " " and num !="\n"]

result = [num for num in num1 if num in num2]

print(result)