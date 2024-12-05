from game import logo, vs
from game import data
import random
import os

def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux
    else:
        os.system('clear')

def format_data(Account):
    account_name = Account["name"]
    account_desc = Account["description"]
    account_country = Account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
Account_b = random.choice(data)

while game_should_continue:
    Account_a = Account_b
    Account_b = random.choice(data)
    while Account_a == Account_b:
        Account_b = random.choice(data)

    print(f"Compare A: {format_data(Account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(Account_b)}.")
    guess = input("Who has more followers? Type 'a' or 'b': ").lower()

    a_follower_count = Account_a["follower_count"]
    b_follower_count = Account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    # Clear the console
    clear()
    if is_correct:
        score += 1
        print(f"Correct answer, your current score is {score}")
    else:
        game_should_continue = False
        print(f"Wrong answer, your final score is {score}")
