# unlimited arguments
# def add(*args): # this function can accept any number of arguments
#     for n in args:
#         print(n)

def add(*args): # makes a tuple of arguments
    sum=0
    for n in args:
        sum+=n
    return sum