from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.paddle_1_score = 0
        self.paddle_2_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.paddle_1_score, align="center", font=("Arial", 40, "normal"))
        self.goto(100, 200)
        self.write(self.paddle_2_score, align="center", font=("Arial", 40, "normal"))

    def paddle_1_point(self):
        self.paddle_1_score += 1
        self.update_score()

    def paddle_2_point(self):
        self.paddle_2_score += 1
        self.update_score()