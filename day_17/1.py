class User:
    def __init__ (self, user_id, username): #constructor
        self.id = user_id 
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user): #all methods must always have self parameter
        user.followers += 1
        self.following += 1

user_1 = User("001", "angela") 
user_2 = User("882", "jack")


user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# dynamic initialization of attributes 
# user_3 = User()
# user_3.id = 3
# user_3.username = "user3"