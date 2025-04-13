# 🎯 Number Guessing Game
# Created by: Sania Irshad

import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\n🎉 Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100.")
    print("Can you guess it? Let's find out!\n")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("🚫 Please guess a number between 1 and 100.")
            elif guess < number:
                print("🔻 Too low! Try again.")
            elif guess > number:
                print("🔺 Too high! Try again.")
            else:
                print(f"🎯 Great job, {attempts} attempts to find the number {number}!")
                break

        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

def main():
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("👋 Thank you for playing! See you next time.")
            break

if __name__ == "__main__":
    main()
