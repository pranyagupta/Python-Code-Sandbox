import turtle
tim = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('black')
tim.color('cyan')

def draw_poly(sides,length):
    for _ in range(sides):
        tim.forward(length)
        tim.left(360/sides)

draw_poly(3,10)

