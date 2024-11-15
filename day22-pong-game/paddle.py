from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.goto(position)

    def on_up(self):
        self.y += 20
        self.goto(self.x, self.y)

    def on_down(self):
        self.y -= 20
        self.goto(self.xcor(), self.y)
