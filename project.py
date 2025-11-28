import random

def number_guessing_game():
    """
    A simple number guessing game where the computer selects a random number
    between 1 and 50 and the user tries to guess it.
    
    """
    while True:
        num = random.randint(1, 50)
        count = 0

        while True:
            guess = int(input("Guess a number between 1 and 50: "))
            count += 1

            if guess > num:
                print("Your guess is Too High\n")
            elif guess < num:
                print("Too Low! Try again.\n")
            else:
                print("\nCorrect! You guessed the number!")
                print("The number was:", num)
                print("Total guesses:", count)
                break

        play = input("\nDo you want to play again? (yes/no): ").lower()

        if play != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Calling The game
number_guessing_game()
