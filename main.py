from art import logo
import random


def set_diffculty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return 10
    else:
        return 5


def check_answer(numb1, numb2, turns):
    if numb1 < numb2:
        print("Too low.")
        return turns - 1
    elif numb1 > numb2:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it! the answer was {numb1}")


def run_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    attempts = set_diffculty()

    guess = 0

    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)

        if attempts == 0:
            print(
                f"You've run out of guesses, you lose. The answer was {answer}")
            break
        elif guess != answer:
            print("Guess again.")


run_game()
