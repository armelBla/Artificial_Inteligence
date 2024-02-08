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
# part of player choice
decision = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for Scissors."))
if decision <= 2:

    game_choice = [rock, paper, scissors]
    print(f"You choose: \n{game_choice[decision]}")

    # part of computer choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: \n{game_choice[computer_choice]}")

    # instruction for winner

    if decision == 0 and computer_choice == 3:
        print(f"you win: {game_choice[0]} beats {game_choice[3]}")
    elif decision == 3 and computer_choice == 2:
        print(f"you win: {game_choice[3]} beats {game_choice[2]}")
    elif decision == 2 and computer_choice == 1:
        print(f"you win: {game_choice[2]} beats {game_choice[1]}")
    elif decision == computer_choice:
        print("replay: Draw")
    else:
        print(f"you Lose: {game_choice[computer_choice]} beats {game_choice[decision]}")
else:
    print("You type invalide number, you have to type number 0, 1 or 2")