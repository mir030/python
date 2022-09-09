from turtle import Turtle, Screen
import pandas


screen = Screen()
turtle = Turtle()
screen.title("US states game")
background_image = "blank_states_img.gif"
screen.addshape(background_image)
turtle.shape(background_image)

data = pandas.read_csv("50_states.csv")
states_list = list(data["state"])

game_is_on = True
correct_guesses = 0
try_count = 0
guessed_states = []
while game_is_on:
    answer_state = str(screen.textinput(f"{try_count}/50 States Correct", "What's another states name?"))
    answer_state = answer_state.capitalize()
    try_count += 1
    if try_count == 50 or answer_state == "Exit":
        game_is_on = False
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")

    if answer_state in states_list:
        correct_guesses += 1
        guessed_states.append(answer_state)
        state_row = data[data["state"] == answer_state]
        x_cor = int(state_row.x)
        y_cor = int(state_row.y)
        t = Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x_cor, y_cor)
        t.write(answer_state)

print(f"You score is {correct_guesses}")