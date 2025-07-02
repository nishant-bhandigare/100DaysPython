# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there were no exceptions
# finally: do this no matter what happens


try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content: file.read()
    print(content)
finally:
    file.close()
    raise TypeError("This is an error that I made up.")