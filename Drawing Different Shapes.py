from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("blue")

colors_list = ['navy', 'dark gray', 'cyan', 'aquamarine', 'steel blue', 'firebrick', 'sandy brown', 'dark orchid', 'yellow', 'dark slate blue', 'medium violet red', 'maroon']

def drawShape(num_sides):
  angle = 360 / num_sides
  for _ in range(num_sides):
    tim.forward(100)
    tim.right(angle)
    

for shape_side in range(3,21):
  tim.color(random.choice(colors_list))
  drawShape(shape_side)

screen = Screen()
screen.bgcolor(0.5,1,0.5)
screen.exitonclick()