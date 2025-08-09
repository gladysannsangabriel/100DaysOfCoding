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

hand_signals = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n   "))
computer_choice = random.randint(0,2)

if your_choice < 0 or your_choice > 2:
    print("Invalid choice!")
else:
    print(hand_signals[your_choice])

    print("Computer chose: ")
    print(hand_signals[computer_choice])

    if your_choice == computer_choice:
        print("It's a draw.")
    elif your_choice == 0 and computer_choice == 2:
        print("You win!")
    elif your_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif your_choice > computer_choice:
        print("You win!")
    elif your_choice < computer_choice:
        print("You lose!")
    else:
        print("Invalid result.")

    # if your_choice == computer_choice:
    #     print("It's a draw.")
    # else:
    #     if your_choice == 0: # rock
    #         if computer_choice == 1: # paper
    #             print("You lose!")
    #         elif computer_choice == 2: # scissors
    #             print("You win!")
    #
    #     elif your_choice == 1: # paper
    #         if computer_choice == 0:  # rock
    #             print("You win!")
    #         elif computer_choice == 2:  # scissors
    #             print("You lose!")
    #
    #     elif your_choice ==2: # scissors
    #         if computer_choice == 0:  # rock
    #             print("You lose!")
    #         elif computer_choice == 1:  # paper
    #             print("You win!")
    #
    #     else:
    #         print("Invalid result.")