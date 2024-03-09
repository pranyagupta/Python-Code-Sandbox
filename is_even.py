def is_even(blah):
    if blah % 2 == 0:
        return True
    else:
        return False

for i in range(1, 11):
    if is_even(i):
        print(i)
    else:
        print("ODD!")
