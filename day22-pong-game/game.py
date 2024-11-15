import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600
X_POSITION = 500
Y_POSITION = 250
PADDLE_1_POSITION = (-350, 0)
PADDLE_2_POSITION = (350, 0)


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT, startx=X_POSITION, starty=Y_POSITION)
        self.screen.title("Pong Game")
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.listen()
        self.paddle_1 = Paddle(PADDLE_1_POSITION)
        self.paddle_2 = Paddle(PADDLE_2_POSITION)
        self.ball = Ball()
        self.scoreboard = Scoreboard()
        self.game_is_on = True
        self.handle_events()

    def handle_events(self):
        self.screen.onkey(self.paddle_1.on_up, "w")
        self.screen.onkey(self.paddle_1.on_down, "s")
        self.screen.onkey(self.paddle_2.on_up, "Up")
        self.screen.onkey(self.paddle_2.on_down, "Down")

    def run_game(self):
        while self.game_is_on:
            time.sleep(self.ball.ball_speed)
            self.screen.update()
            self.ball.move()

            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce_y()

            if (
                    self.ball.distance(self.paddle_1) < 50 and self.ball.xcor() < -320
                    or self.ball.distance(self.paddle_2) < 50 and self.ball.xcor() > 320
            ):
                self.ball.bounce_x()

            if self.ball.xcor() > 380:
                self.ball.reset()
                self.scoreboard.paddle_1_point()

            if self.ball.xcor() < -380:
                self.ball.reset()
                self.scoreboard.paddle_2_point()

        self.screen.exitonclick()
