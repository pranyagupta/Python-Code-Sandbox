year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 != 0:
        print("Leap Year")
    elif year % 400 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")   
else:
    print("Not a leap year")
    
    
