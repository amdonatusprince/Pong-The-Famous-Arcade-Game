from turtle import Turtle

SCORE_FONT_SIZE = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(arg=self.l_score, align="center", font=SCORE_FONT_SIZE)
        self.goto(x=100, y=200)
        self.write(arg=self.r_score, align="center", font=SCORE_FONT_SIZE)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()