from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(10)

screen = Screen()
screen.colormode(255)


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def randomChoice():
   direnction = [0, 90 ,180, 270]
   return random.choice(direnction)


screen.bgcolor((180, 196, 255))
for _ in range(200):
  tim.forward(30)
  tim.color(randomColor())
  tim.setheading(randomChoice())


screen.exitonclick()
