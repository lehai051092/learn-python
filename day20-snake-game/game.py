import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.tracer(0)
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.screen.listen()
        self.game_is_on = True
        self.handle_events()

    def handle_events(self):
        self.screen.onkey(self.snake.up, "w")
        self.screen.onkey(self.snake.up, "up")
        self.screen.onkey(self.snake.down, "s")
        self.screen.onkey(self.snake.down, "down")
        self.screen.onkey(self.snake.left, "a")
        self.screen.onkey(self.snake.left, "left")
        self.screen.onkey(self.snake.right, "d")
        self.screen.onkey(self.snake.right, "right")

    def run_game(self):
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            if self.snake.head.distance(self.food) < 17:
                self.scoreboard.increase_score()
                self.snake.extend_segment()
                self.food.refresh()

            if self.snake.head.xcor() > 280 or self.snake.head.xcor() < -280 or self.snake.head.ycor() > 280 or self.snake.head.ycor() < -280:
                self.game_is_on = False
                self.scoreboard.game_over()

            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.game_is_on = False
                    self.scoreboard.game_over()

        self.screen.exitonclick()
