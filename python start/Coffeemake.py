# Car class definition
class Car:
    def printing(self):
        print("hell")


# User class definition
class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Creating an instance of Car
user_car = Car()
user_car.printing()  # Output: hell

# Creating users
user1 = User(1, "Alice")
user2 = User(2, "Bob")

# User1 follows User2
user1.follow(user2)

# Printing results
print(f"{user1.name} is following {user1.following} user(s) and has {user1.followers} follower(s).")
print(f"{user2.name} is following {user2.following} user(s) and has {user2.followers} follower(s).")
