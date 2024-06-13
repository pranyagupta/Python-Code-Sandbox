# import rndom module
import random
#get a symbol for each rock paper and scissors. 
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

#Write your code below this line 👇
#create a list which has the symbols for rps.

rps = [rock, paper, scissors]

#give a score whih is initialy 0.
score = 0
#create an infinite loop.
while True:
#take a choice from user for each rps in int form.
    user_choice = int(
        input(
            "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
        ))
    
##generate a comuters choice .
    comp_choice = random.randint(0, 2)
## give conditions for the game using if and else statement.
    if user_choice < 0 or user_choice > 2:
      print("You typed an invalid number")
    else:
      print(f"You chose: {rps[user_choice]}")
      print(f"Computer chose: {rps[comp_choice]}")

    if user_choice == 0 and comp_choice == 0:
        print("Game Draw!")
        print(f"Score: {score}")
    if user_choice == 1 and comp_choice == 1:
        print("Game Draw!")
        print(f"Score: {score}")
    if user_choice == 2 and comp_choice == 2:
        print("Game Draw!")
        print(f"Score: {score}")

    if user_choice == 0 and comp_choice == 2:
        print("You Win!")
        score += 1
        print(f"Score: {score}")
    if user_choice == 1 and comp_choice == 0:
        print("You Win!")
        score += 1
        print(f"Score: {score}")
    if user_choice == 2 and comp_choice == 1:
        print("You Win!")
        score += 1
        print(f"Score: {score}")

    if user_choice == 0 and comp_choice == 1:
        print("You Lose!")
        score -= 1
        print(f"Score: {score}")
    if user_choice == 1 and comp_choice == 2:
        print("You Lose!")
        score -= 1
        print(f"Score: {score}")
    if user_choice == 2 and comp_choice == 0:
        print("You Lose!")
        score -= 1
        print(f"Score: {score}")

