# How to Iterate over a Pandas DataFrame

import pandas as pd

student_dict = {
    "student" : ["Angela", "Jack", "Lily"],
    "score" : [56,76,98]
}

# looping through dictionaries
for (key, value) in student_dict.items():
    print(key)

for (key, value) in student_dict.items():
    print(value)

# print(student_dict.items())

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# looping through a dataframe
for (key, value) in student_data_frame.items(): 
    print(key) # gives titles of columns


for (key, value) in student_data_frame.items():
    print(value) # gives contents of columns

# loop through rows of the dataframe
for (index, row) in student_data_frame.iterrows():
    # print(row) # pandas series object
    print(row.student)

    if(row.student == "Angela"):
        print(row.score)