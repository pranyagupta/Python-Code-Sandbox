import turtle

wn = turtle.Screen()
rondu = turtle.Turtle()

turtle.speed(0)
def draw_circle1():
    for _ in range(360):
        rondu.forward(1)
        rondu.left(1)

draw_circle1()

wn.exitonclick()
