import turtle
import pandas


screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states = pandas.read_csv("50_states.csv")
is_running = True
all_states = states.state.to_list()
guessed_states = []
count = 0

while is_running:
    guess = turtle.textinput(f"States Correct {len(guessed_states)}/{len(all_states)}", "What's another state name?").title()
    if guess is None:
        is_running = False
        turtle.bye()


    if guess in all_states and guess not in guessed_states:
        obj = turtle.Turtle()
        obj.hideturtle()
        obj.penup()
        state = states[states['state'] == guess]
        obj.goto(state.x.item(), state.y.item())
        obj.write(guess)
        guessed_states.append(guess)

    count += 1

    if count == len(all_states):
        missing_data = []
        for item in all_states:
            if item not in guessed_states:
                missing_data.append(item)

        missing_states = pandas.DataFrame(missing_data)
        missing_states.to_csv("missing_data.csv")
        is_running = False
        turtle.bye()

screen.mainloop()

