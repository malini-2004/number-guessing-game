import random

# Function to play the game
def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    
    # Get range from user
    try:
        lower = int(input("Enter the lower bound of the range: "))
        upper = int(input("Enter the upper bound of the range: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    # Generate a random number within the range
    number_to_guess = random.randint(lower, upper)
    attempts = 0
    guessed = False

    print(f"\nI'm thinking of a number between {lower} and {upper}. Can you guess it?")

    # Game loop
    while not guessed:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempt(s).")
        except ValueError:
            print("Please enter a valid number.")

# Main game controller
def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
