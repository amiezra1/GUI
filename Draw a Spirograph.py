from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

screen = Screen()
screen.colormode(255)


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.speed(0)
def darwSpirograph(siz_of_gap):
  for _ in range(int(360 / siz_of_gap)):
    tim.color(randomColor())
    tim.circle(100)
    tim.setheading(tim.heading() + siz_of_gap)

darwSpirograph(2)

screen.exitonclick()