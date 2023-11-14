from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(0, 0)
        self.write("You won", align="center",font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("You lost, Boooo", align="center", font=FONT)
