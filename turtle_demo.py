import turtle
import random

twinklles = turtle.Turtle()

wn = turtle.Screen()
twinklles.shape("triangle")


twinklles.pendown()

distance = random.randint(0, 100)
angle = random.randint(0, 360)

while True:

    twinklles.fd(distance)
    twinklles.left(angle)

wn.exitonclick()
