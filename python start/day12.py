import random

def number_guessing():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    
    guessed_correctly = False
    
    # Define difficulty levels
    def easy():
        return 10  # 10 attempts for easy level
    
    def hard():
        return 5  # 5 attempts for hard level

    # Ask the user to select a difficulty level
    level = input("Choose a difficulty level: 'easy' or 'hard': ").lower()
    if level == "hard":
        attempts = hard()
    else:
        attempts = easy()

    # Main game loop
    while not guessed_correctly and attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        
        # User makes a guess
        make_a_guess = int(input("Make a guess: "))
        attempts -= 1  # Reduce attempts after every guess

        # Provide feedback on the guess
        if make_a_guess > number:
            print("Too high.")
        elif make_a_guess < number:
            print("Too low.")
        else:
            print(f"Congratulations! You guessed the number {number} correctly.")
            guessed_correctly = True  # End the game if the guess is correct

    # End of game feedback if out of attempts
    if not guessed_correctly:
        print(f"Sorry, you've run out of attempts. The number was {number}.")

# Start the game
number_guessing()
