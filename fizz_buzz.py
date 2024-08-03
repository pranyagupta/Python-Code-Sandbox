a=int(input("Enter a number: "))
if a%3==0 and a%5==0:
    print("fizz_buzz")

elif a%3==0:
    print("fizz")
elif a%5==0:
    print("buzz")
else:
    print(a)
