from turtle import Turtle, Screen
import random

colors = ["red", "green", "yellow", "blue", "purple", "orange"]
y_positions = [90, 60, 30, -30, -60, -90]
all_turtles = []
game_on = False

screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(title="Make a bet",
                            prompt="Whick turtle is gonna win the race?: ")

if user_bet:
  game_on = True

for index in range(0, 6):
  tim = Turtle("turtle")
  tim.penup()
  tim.goto(-230, y_positions[index])
  tim.color(colors[index])
  all_turtles.append(tim)

while game_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      game_on = False
      winning_turtle = turtle.pencolor()
      if winning_turtle == user_bet:
        print(f"You have won! The {winning_turtle} turtle has reached first.")
      else:
        print(f"You have lost! The {winning_turtle} turtle has reached first.")
    turtle.forward(random.randint(0, 10))
