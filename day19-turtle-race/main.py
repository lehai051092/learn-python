from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet = screen.textinput(
    title="Make your bet",
    prompt=f"Which turtle will win the race? Enter a color ({', '.join(colors)})"
).lower()
turtles = []
space = 0
speeds = [10, 20, 30]
is_started = False

for color in colors:
    obj = Turtle(shape='turtle')
    obj.color(color)
    obj.penup()
    obj.goto(x=-230, y= 100 - space)
    obj.speed("slow")
    space += 30
    turtles.append(obj)

if user_bet:
    is_started = True

while is_started:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_started = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        else:
            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)


screen.exitonclick()