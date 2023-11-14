import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()
game_is_on = True
screen.listen()
screen.onkey(player.go_up, "Up")

while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move_car()
    if car.detect_collision(player):
        scoreboard.game_over()
        game_is_on = False
    if player.ycor() > 280.00:
        scoreboard.update_scoreboard()
    screen.update()


screen.exitonclick()