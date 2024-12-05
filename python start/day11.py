import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    # Check for a blackjack (Ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Check if there's an Ace and the score is over 21, replace Ace from 11 to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_cards = []
computer_cards = []
is_game_over = False

# Deal two cards to both the user and the computer
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    # Check for game over conditions (Blackjack or bust)
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_deal = input("Type 'y' to get a new card or 'n' to pass: ")
        if user_deal == "y":
            user_cards.append(deal_card())  # Add a new card for the user
            user_score = calculate_score(user_cards)  # Recalculate score
            if user_score > 21:
                is_game_over = True  # End the game if the user busts
        else:
            is_game_over = True

# Computer's turn (if user didn't bust or get Blackjack)
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

# Determine the winner
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose!"
    elif user_score == 0:
        return "You have Blackjack! You win!"
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

print(f"\nYour final cards: {user_cards}, final score: {user_score}")
print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))
