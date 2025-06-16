# DICTIONARY COMPREHENSION
import random

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student:random.randint(1,100) for student in students}

print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score>=60}

print(passed_students)