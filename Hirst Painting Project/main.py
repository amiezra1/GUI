# from turtle import Turtle, Screen
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.shape("turtle")
tim.speed(0)
tim.penup()
tim.hideturtle()
color_list = [(207, 155, 102), (57, 107, 128), (162, 82, 43), (125, 79, 97), (122, 156, 171), (126, 175, 159), (195, 142, 39), (226, 198, 130), (188, 89, 109), (191, 131, 145), (14, 44, 57), (53, 38, 19), (51, 164, 128), (59, 121, 114), (218, 90, 70), (159, 22, 32), (41, 31, 33), (8, 30, 28), (81, 146, 165), (238, 167, 162), (156, 28, 21), (23, 80, 91), (233, 168, 173), (173, 206, 188), (106, 126, 157), (26, 87, 84)]

screen = turtle_module.Screen()
screen.bgcolor((180, 196, 255))

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1 , num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen.exitonclick()