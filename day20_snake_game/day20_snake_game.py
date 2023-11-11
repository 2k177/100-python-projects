from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# nag = Turtle()
# nag.color("white")
# nag.shape("square")
segment_list = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segment_list.append(new_segment)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segment_list:
    #     seg.forward(20)
    for seg_num in range(len(segment_list)-1 , 0, -1 ):
        new_x = segment_list[seg_num-1].xcor()
        new_y = segment_list[seg_num-1].ycor()
        segment_list[seg_num].goto(new_x, new_y)
    segment_list[0].forward(20)

screen.exitonclick()