from turtle import Turtle, Screen

from shapes import draw_square, draw_dashed_line, draw_different_shapes

turtle = Turtle()

turtle.shape('turtle')

# draw_square(turtle)
# draw_dashed_line(turtle)
draw_different_shapes(turtle, 100)

screen = Screen()
screen.exitonclick()
