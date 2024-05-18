import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fast")
# screen = t.Screen()

# screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)


def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(10):
  for _ in range(10):
    # tim.pendown()
    # tim.color(random_color())
    # tim.begin_fill()
    # tim.circle(20)
    # tim.end_fill()
    # tim.penup()
    # tim.forward(50)
    # tim.pendown()
    tim.dot(20, random_color())
    tim.forward(50)
  tim.setheading(90)
  tim.forward(50)
  tim.setheading(180)
  tim.forward(500)
  tim.setheading(0)
  
# screen.exitonclick()
