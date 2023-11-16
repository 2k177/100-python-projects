import turtle
import pandas

screen = turtle.Screen()
# turtle  = turtle.Turtle()
screen.setup(height=491, width=725)
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"({len(guessed_states)}/50)Guess the State", prompt="Whats other state name?")

    if answer_state == "Exit":
        # remaining_data = state_data[~state_data['state'].isin(guessed_states)]
        remaining_data = data[~data.state.str.contains('|'.join(guessed_states))]
        print(remaining_data)
        remaining_data.to_csv("states_to_learn.csv")
        break
    if answer_state.title() in all_states:
        guessed_states.append(answer_state.title())
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state.title()]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(f"{answer_state}")
        print(guessed_states)
screen.mainloop()
