from turtle import Screen, Turtle

wn = Screen()
wn.bgcolor("black")

gupchup = Turtle()
gupchup.shape("turtle")

gupchup.color("cornsilk")
gupchup.pensize(5)

gupchup.penup()
gupchup.backward(150)
gupchup.pendown()

for _ in range(5):
    gupchup.forward(300)
    gupchup.right(144)


wn.exitonclick()
