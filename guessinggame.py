import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the guessing game
guessing_game()
