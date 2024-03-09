# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(weight/height**2)

print("Your BMI is", bmi)

if bmi<18:
    print("under weight")
elif bmi>=18 and bmi<25:
    print("normal weight")
elif bmi>=25 and bmi<30:
    print("over weight")
else:
    print("obese")
