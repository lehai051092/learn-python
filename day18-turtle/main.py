##### turtle challenge

import turtle as t

from random import choice, randint
from symbol import return_stmt

from shapes import draw_square, draw_dashed_line, draw_different_shapes, draw_random_walk, draw_spirograph, \
    draw_hirst_spot_painting

turtle = t.Turtle()
t.colormode(255)
screen = t.Screen()
#
# turtle.shape('turtle')

# draw_square(turtle)
# draw_dashed_line(turtle)
# draw_different_shapes(turtle, 100)
# draw_random_walk(turtle)
# draw_spirograph(turtle, 5)


##### The Hirst Painting Project
# import colorgram
#
# colors = colorgram.extract('hirst-spot-painting.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

draw_hirst_spot_painting(turtle, 10, 5, 20, 40)

screen.exitonclick()
