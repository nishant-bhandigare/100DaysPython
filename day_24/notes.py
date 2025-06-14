file = open("day_24/my_file.txt") #opens the file
contents =  file.read() #read method returns the contents of the file
print(contents)
file.close() #after all tasks are done we also have to close the file, because we don't when or will python close the file and free up the resources


with open("day_24/my_file.txt") as file: #here we do not need to remember to close the file
    contents =  file.read()
    print(contents)

# with open("day_24/my_file.txt") as file:
#     file.write("New Text.") # cannot do this because we opened the file in read only mode
#     print(contents)

with open("day_24/my_file.txt", mode = "w") as file: #default mode is read
    file.write("New Text.") #deletes everything written in the file, if file does not exist then file is created
    print(contents)

with open("day_24/my_file.txt", mode = "a") as file: #default mode is read
    file.write("More New Text.") #appends new content to the file 
    print(contents)