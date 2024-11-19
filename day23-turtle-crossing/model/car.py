from turtle import Turtle


class Car(Turtle):
    def __init__(self, color, y_pos):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x=300, y=y_pos)