from art import logo7
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5


def set_difficulty():
    choose = True
    while choose:
        x = input("choose a difficulty. Type 'easy' or 'hard': ").lower()
        if x == "easy":
            return EASY_LEVEL
            choose = False
        elif x == "hard":
            return HARD_LEVEL
            choose = False
        else:
            print("Please choose correct options")


def check_answer(guess, num, turn):

    if guess > num:
        print("Too high.")
        return turn - 1
    elif guess < num:
        print("Too low.")
        return turn - 1
    else:
        print(f"You got it! The answer was {num}")


def game():
    print(logo7)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 and 100")

    num = randint(1, 100)
    print(f"Pssst, the correct answer is {num}") ## You might need to opt out

    turn = set_difficulty()
    guess = 0
    while guess != num:
        print(f"You have {turn} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        turn = check_answer(guess, num, turn)
        if turn == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != num:
            print("Guess again")

game()