import turtle           ​
t = turtle.Turtle()
wn = turtle.Screen()

​list1 = ["purple","red","orange","blue","green"]
​wn.bgcolor("black") 
for i in range(200):
    ​t.color(list1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    ​t.left(59)
