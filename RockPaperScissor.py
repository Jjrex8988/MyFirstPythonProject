import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
con = True
while con:
    game_images = [rock, paper, scissors]

    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    while user_choice >= 3:
        print("You typed and invalid number")
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice > computer_choice:
        if user_choice - computer_choice == 1:
            print("You win!")
        elif user_choice - computer_choice == 2:
            print("You lose!")
        elif user_choice - computer_choice == -1:
            print("You lose!")
    elif computer_choice > user_choice:
        if computer_choice - user_choice == 1:
            print("You lose!")
        elif computer_choice - user_choice == 2:
            print("You win!")
        elif computer_choice - user_choice == -1:
            print("You win!")
    elif computer_choice == user_choice:
        print("Draw!")

    x = input("Do you want to continue? 'y' or 'n': ").lower()

    if x == "y":
        con = True
    else:
        print("Bye!")
        con = False


