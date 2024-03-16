n=int(input("enter a hieght"))
for i in range(n):
    #Insert spaces in the beginnng for each row
    a_row = " "*(n-(i+1))
    #Insert Bricks
    a_row = a_row + "#"*(i+1)
    #Print the row
    print(a_row)
