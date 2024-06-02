import random

random_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Enter the number I have in mind: "))

    if guess == random_number:
        attempts += 1
        print(f"You guesed the correct number! You took {attempts} attempts to guess the number.")
        break

    elif guess > random_number:
        attempts += 1
        print("Think a smaller number.")

    elif guess < random_number:
        attempts += 1
        print("Think a greater number.")
