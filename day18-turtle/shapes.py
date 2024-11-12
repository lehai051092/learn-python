from random import choice, randint


def draw_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dashed_line(turtle):
    for step in range(100):
        if step % 2 == 0:
            turtle.pendown()
        else:
            turtle.penup()
        turtle.forward(5)


def draw_different_shapes(turtle, size):
    colors = {
        "3": "#000000",
        "4": "#ADD8E6",
        "5": "#40E0D0",
        "6": "#2E8B57",
        "7": "#7CFC00",
        "8": "#A0522D",
        "9": "#DC143C",
    }

    for step in range(3, 10):
        step_string = str(step)
        num_sides = 360 / step
        turtle.fillcolor(colors[step_string])
        turtle.color(colors[step_string])

        for i in range(step):
            turtle.forward(size)
            turtle.right(num_sides)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def draw_random_walk(turtle):
    directions = [0, 90, 180, 270]
    turtle.pensize(15)
    turtle.speed("fastest")

    for _ in range(200):
        turtle.color(random_color())
        turtle.forward(30)
        turtle.setheading(choice(directions))


def draw_spirograph(turtle, size_of_gap):
    turtle.speed("fastest")

    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


def draw_hirst_spot_painting(turtle, rows, columns, size, distance):
    turtle.speed("fastest")
    turtle.hideturtle()
    turtle.penup()
    color_list = [
        (254, 254, 253), (219, 254, 237), (84, 254, 155), (173, 146, 118), (254, 250, 254), (245, 39, 191),
        (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176),
        (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0), (254, 147, 146), (253, 71, 70),
        (244, 248, 254),
        (39, 249, 42), (85, 249, 253), (240, 1, 13), (5, 210, 216), (230, 126, 190), (2, 2, 107),
        (135, 152, 220),
        (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)
    ]
    number_of_dots = rows * columns
    dot_current = columns

    turtle.setheading(255)
    turtle.forward(300)
    turtle.setheading(0)

    for dot_count in range(1, number_of_dots + 1):
        turtle.dot(size, choice(color_list))
        turtle.forward(distance)

        if dot_current == dot_count:
            turtle.setheading(90)
            turtle.forward(distance)
            turtle.setheading(180)
            turtle.forward(distance * columns)
            turtle.setheading(0)

            dot_current += columns
