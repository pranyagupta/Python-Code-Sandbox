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

#Write your code below this line 👇
rps = [rock, paper, scissors]

score = 0

while True:
    user_choice = int(
        input(
            "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
        ))
    comp_choice = random.randint(0, 2)

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

