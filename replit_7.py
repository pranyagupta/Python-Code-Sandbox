import random
coin=random.randint(0,1)
user_choice=int(input("0 for heads & 1 for tails"))
if coin==user_choice:
    if coin == 0:
        print("Heads! You guessed it right.")
    elif coin == 1:
        print("Tails! You guessed it right.")
else:
    if coin == 0:
        print(f"Sorry,you lose.it was Heads!")
    elif coin == 1:
        print(f"Sorry,you lose.it was Tails!")
