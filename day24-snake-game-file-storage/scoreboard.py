from turtle import Turtle
import os
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
SCORE_CARD = "score_card.txt"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align=ALIGNMENT,
                   font=FONT)

    def store_highscore(self):
        with open(SCORE_CARD, "w") as file:
            file.write(f"{self.high_score}")

    def get_highscore(self):
        if os.path.exists(SCORE_CARD):
            with open(SCORE_CARD) as file:
                content = file.read()
            print(content.strip())
            return int(content.strip())
        else:
            return 0

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.store_highscore()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()