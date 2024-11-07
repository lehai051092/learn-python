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
