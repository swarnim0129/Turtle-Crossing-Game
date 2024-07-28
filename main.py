import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager=CarManager()
screen.listen()
screen.onkey(player.go_up, "Up")
scoreboard=Scoreboard()
scoreboard.level_up()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False

    if player.is_at_finish():
        player.back_to_start()
        scoreboard.level_up()
        car_manager.increase_speed()

screen.exitonclick()