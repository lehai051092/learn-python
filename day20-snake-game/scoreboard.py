from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")


def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))


def get_high_score():
    with open("high_score.txt", "r") as file:
        score = int(file.read())

    return score


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score} | Highest Score = {self.high_score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1

        if self.score > self.high_score:
            self.high_score = self.score
            save_high_score(self.high_score)

        self.clear()
        self.update_scoreboard()
