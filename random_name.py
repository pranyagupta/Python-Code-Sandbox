import random

names = input("Enter the names with a space in between: ")
name_list = names.split()

random_name = random.choice(name_list)

print(f"Hello stupid, {random_name}!")
