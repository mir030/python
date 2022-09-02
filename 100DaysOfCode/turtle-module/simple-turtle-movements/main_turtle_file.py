import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim = Turtle()
tim.shape("turtle")
tim.speed(25)

"""Drawing a square"""
# for _ in range(0, 4):
#     tim.forward(100)
#     tim.left(90)

"""Drawing a dashed line"""
# for _ in range(0, 15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

"""Drawing 10 different shapes"""
# for i in range(3, 11):
#     angle = 360 / i
#     pen_color = ["black", "purple", "gold", "grey", "brown", "red", "yellow", "green"]
#     tim.pencolor(random.choice(pen_color))
#     for j in range(0, i):
#         tim.forward(100)
#         tim.right(angle)

""" Draw a Random Walk"""
turtle.colormode(255)
# angle_degree = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(40)
#
# for _ in range(0, 100):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(angle_degree))

"""Draw a spirograph"""
# for i in range(1, 101):
#     tim.color(random_color())
#     tim.circle(100)
#     tilt = 360 / 100
#     tim.setheading(tilt * i)

screen = Screen()
screen.exitonclick()