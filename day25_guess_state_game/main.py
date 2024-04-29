import pandas as pd
import turtle as tur

states = pd.read_csv('/mnt/c/Dev/python_learning/day25_guess_state_game/50_states.csv')

s = tur.Screen()
s.setup(720, 480)

bg = '/mnt/c/Dev/python_learning/day25_guess_state_game/blank_states_img.gif'
s.addshape(bg)
tur.shape(bg)
t = tur.Turtle()
t.hideturtle()
t.penup()
t.color("black")
answered = []
msg = "Guess state name"

game_on = True

while game_on:
    guess = tur.textinput("State {}/{}".format(len(answered), len(states)), msg)
    row = states[states.state.str.lower() == guess.lower()]
    if guess in answered:
        msg = "Already answered"
    elif not row.empty:
        msg = "Correct! Guess another one"
        t.goto(int(row.x.iloc[0] - 20), int(row.y.iloc[0]))
        t.write(row.state.iloc[0])
        answered.append(row.state.iloc[0].lower())
        
        if len(answered) == len(states):
            game_on = False
    else:
        msg = "Wrong"

tur.textinput("Congratulations!!!", "You've correctly guessed all the states!")
s.exitonclick()
