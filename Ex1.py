import math

a = int(input("Enter one side: "))
b = int(input("enter second side : "))
c = int(input("enter third side : "))

s = (a+b+c)/2

#print(s)

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Area of the triangle is: ", area)
