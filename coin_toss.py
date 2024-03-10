import random

score = 0

while(True):
    coin = random.randint(0,1)
    user_choice = int(input("Choose Head or Tails, 0 for tails and 1 for heads: "))
    if coin == 0:
        print("Tails")
        if user_choice == 0:
            score += 1
            print(f"Tails it is! You scored {score}.")
        else:
            print(f"You were not correct! You scored {score}.")
            break
    elif coin == 1:
        print("Heads")
        if user_choice == 1:
            score += 1
            print(f"Heads it is! You scored {score}.")
        else:
            print(f"You were not correct! You scored {score}.")
            break
        
