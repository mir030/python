import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.up, "Up")

car = CarManager()
score = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    # reset turtle to original position and speed up the cars
    if player.is_at_finish():
        score.screen_update()
        player.reset_position()
        # increase car speed
        car.level_up()

    # Detect collision with turtles
    for single_car in car.all_cars:
        if player.distance(single_car) < 30:
            game_is_on = False
            score.game_over()

screen.exitonclick()