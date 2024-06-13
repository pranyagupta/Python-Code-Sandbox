import random
#let comp choose a random number from 1 upto 100.
random_number = random.randint(1, 100)
attempts = 0
#start a infinite loop
while True:
    #user input for the number
    guess = int(input("Enter the number I have in mind: "))

    #give a condition that if your num and comp num are same print you win and break.
    if guess == random_number:
        attempts += 1
        print(f"You guesed the correct number! You took {attempts} attempts to guess the number.")
        break
    #give a condition that if your num is greater than the comp num print a "smaller number pls" and increase attempts by 1.
    elif guess > random_number:
        attempts += 1
        print("Think a smaller number.")
    #give a condition that if your num is smaller than the comp num  print "a greater number pls" and increase attempts by 1.
    elif guess < random_number:
        attempts += 1
        print("Think a greater number.")
