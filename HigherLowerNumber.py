from game_data import data
from art import logo8, vs
import random
from replit import clear


def format_data(account):
    account_name = account['name']
    account_descr = account["description"]
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"


def checking_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo8)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A : {format_data(account_a)}.")

    print(vs)

    print(f"Against B : {format_data(account_b)}.")

    # guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    guess = 'x'
    while guess not in ['a', 'b']:
        print("Please Type 'A' or 'B' only")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == 'a' or guess == 'b':
            game_should_continue = True

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = checking_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo8)

    if is_correct:
        score += 1
        # if a_follower_count > b_follower_count:
        #     account_b = random.choice(data)
        #
        # else:
        #     account_a = random.choice(data)

        print(f"You're right! Current score: {score}")

    elif not is_correct:
        # if b_follower_count > a_follower_count:
        #     account_a = random.choice(data)
        #
        # else:
        #     account_b = random.choice(data)

        print(f"Sorry, that's wrong. Final score: {score}")

        ask = input("Do you want to play again? 'y' or 'n': ").lower()
        while ask not in ['y', 'n']:
            print("Please insert choose correctly: ")
            ask = input("Do you want to play again?? 'y' or 'n': ").lower()
            if ask == 'y':
                game_should_continue = True
            elif ask == 'n':
                game_should_continue = False

        if ask == 'y':
            game_should_continue = True
        elif ask == 'n':
            game_should_continue = False
            print(f"Final score: {score}")
