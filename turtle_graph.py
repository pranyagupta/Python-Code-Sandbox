import turtle as t
from random import randint
tim = t.Turtle()
t.colormode(255)
tim.speed("fast")
def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)
  
for _ in range(0, 36):
  color = random_color()
  tim.color(color)
  tim.circle(50)
  tim.left(10)
