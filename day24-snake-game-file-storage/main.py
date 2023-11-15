from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_obj = Snake()
food_obj = Food()
score_obj = ScoreBoard()
game_is_on = True
screen.listen()
screen.onkey(snake_obj.up, "Up")
screen.onkey(snake_obj.down, "Down")
screen.onkey(snake_obj.left, "Left")
screen.onkey(snake_obj.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_obj.move()

    #detect collision with food
    if snake_obj.head.distance(food_obj) < 15:
        food_obj.refresh()
        snake_obj.extend()
        score_obj.increase_score()

    #detect collision with wall
    if snake_obj.head.xcor() > 280 or \
            snake_obj.head.xcor() < -280 or \
            snake_obj.head.ycor() > 280 or \
            snake_obj.head.ycor() < -280:
        # game_is_on = False
        score_obj.reset()
        snake_obj.reset()


    #detect the collision of snake tail
    for segment in snake_obj.segments:
        if segment == snake_obj.head:
            pass
        elif snake_obj.head.distance(segment) < 10:
            # game_is_on = False
            score_obj.reset()
            snake_obj.reset()

screen.exitonclick()