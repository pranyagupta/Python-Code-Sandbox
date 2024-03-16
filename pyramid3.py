n=int(input("enter a hieght: "))
for i in range(n):
    #create a row with beginning spaces
    a_row = " "*(n-(i+1))
    #add to the row the bricks for the first pyramid
    a_row = a_row + "#"*(i+1)
    #add two spaces to the row
    a_row = a_row + "  "
    #add the last peice of bricks at the end
    a_row = a_row + "#"*(i+1) 
    #print the row
    print(a_row)
