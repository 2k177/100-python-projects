import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter the color: ")

color_list = ["red", "blue", "purple", "pink", "brown", "orange"]
turtle_objs = []
y_axis = 75

for i in range(len(color_list)):
    turtle_objs.append(Turtle(shape="turtle"))
    turtle_objs[i].color(color_list[i])
    turtle_objs[i].penup()
    turtle_objs[i].goto(x=-249, y=y_axis)
    y_axis -= 25

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_objs:
        if turtle.xcor() >= 245:
            winning_color = turtle.pencolor()
            if user_bet.lower() == winning_color:
                print(f"You've Won !! the {winning_color} turtle is the winner")
            else:
                print(f"You've lost !! the {winning_color} turtle is the winner")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()