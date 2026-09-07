
import random

def number_guess_game():
    print("Welcome to the Number Guessing Game")
    print("I have selected a number between 1 and 20.")

    number_to_guess = random.randint(1, 20)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess == number_to_guess:
            print(f"congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break 
        elif guess < number_to_guess:
            print(" Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print(f"Sorry , you've used all {max_attempts} attempts. The number was {number_to_guess}.")


    #ask if user wants ro play again 
    play_again = input(" Do you want to play again ? (yes/no): "). lower()
    if play_again in['yes', 'y']:
        number_guess_game()
    else:
        print("Thank you for playing! Goodbye!")

if __name__ == "__main__":
    number_guess_game()