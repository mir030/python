# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
#
# colors_list = []
# for color in colors:
#     rgb = color.rgb
#     colors_list.append((rgb.r, rgb.g, rgb.b))
#
# print(colors_list)
from turtle import Turtle, Screen
import random
import turtle

color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
              (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
              (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28),
              (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210),(146, 216, 199), (179, 17, 8),
              (233, 66, 34)]

turtle.colormode(255)
tim = Turtle()
tim.speed(50)
tim.hideturtle()
tim.penup()
tim.goto(-180, -180)
for _ in range(0, 10):
    for _ in range(0, 10):
        random_color = random.randint(0, len(color_list)-1)
        tim.color(color_list[random_color])
        tim.dot(20)
        tim.forward(50)

    current_x_position = tim.position()[1]
    tim.goto(-180, current_x_position + 50)


screen = Screen()
screen.exitonclick()