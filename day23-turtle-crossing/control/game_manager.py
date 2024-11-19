import time
from turtle import Screen

from control.car_manager import CarManager
from model.player import Player
from model.scoreboard import Scoreboard


class GameManager:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.player = Player()
        self.car_manager = CarManager()
        self.scoreboard = Scoreboard()
        self.screen.listen()
        self.register_events()
        self.game_is_on = True

    def register_events(self):
        self.screen.onkey(self.player.go_up, "Up")
        self.screen.onkey(self.player.go_up, "w")

    def run(self):
        while self.game_is_on:
            time.sleep(0.1)
            self.screen.update()

            self.car_manager.create_car()
            self.car_manager.move_cars()

            # Detect collision with car
            for car in self.car_manager.all_cars:
                if car.distance(self.player) < 20:
                    self.game_is_on = False
                    self.scoreboard.game_over()

            # Detect successful crossing
            if self.player.is_at_finish_line():
                self.player.go_to_start()
                self.car_manager.level_up()
                self.scoreboard.increase_level()

        self.screen.exitonclick()
