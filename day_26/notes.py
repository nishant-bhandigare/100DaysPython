# LIST COMPREHENSION

numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)

# list comprehension
# new_list = [new_item for item in list]

new_list = [n+1 for n in numbers]
print(new_list)

name  = "Angela"
new_list = [letter for letter in name]
print(new_list)

# python sequences
# list
# range
# string
# tuple

new_list = [n*2 for n in range(1,5)]
print(new_list)

# conditional list comprehension
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name)<5]
print(short_names)

long_names_upper = [name.upper() for name in names if len(name)>5]
print(long_names_upper)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num%2 == 0]
print(result)