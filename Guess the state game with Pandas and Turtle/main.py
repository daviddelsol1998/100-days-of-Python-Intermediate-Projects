#import libraries
import turtle
import pandas

# read csv file
states_file = pandas.read_csv('50_states.csv')

# keep track of the guessed states
states_guessed = []

# screen setup
screen = turtle.Screen()
screen.title('Guess all the States game (Turtle and Pandas project)')
screen.setup(730, 495)
screen.bgpic('blank_states_img.gif')


# play the game until all 50 states have been guessed
while len(states_guessed) < 50:
    # handle user input standarized in uppercase
    user_guess = turtle.textinput(
        title=f'{len(states_guessed)}/50', prompt='Please enter a state name')
    user_guess = user_guess.upper()  # get it in all caps for comparison purposes

    if user_guess == 'EXIT':
        print('hi')
        states_to_learn = []
        for state in states_file.state:
            if state not in states_guessed:
                states_to_learn.append(state)

        states_to_learn_dict = {
            'state': states_to_learn
        }

        states_to_learn_df = pandas.DataFrame(states_to_learn_dict)

        states_to_learn_df.to_csv(f'states_to_learn.csv')

    # loop through states
    for state in states_file.state:
        if state.upper() == user_guess:  # check for correct guesses
            # update the states guessed
            states_guessed.append(user_guess.title())
            # display the state name in the map
            # setup state turtle
            state_turtle = turtle.Turtle()
            state_turtle.penup()
            state_turtle.hideturtle()
            # get location of x and y for state
            state_row = states_file[states_file.state == user_guess.title()]
            x = int(state_row.x.to_string(index=False))
            y = int(state_row.y.to_string(index=False))
            # display name in map
            state_turtle.goto(x, y)
            state_turtle.write(user_guess.title())

            print(states_guessed)

# keep screen open until the user closes the program
screen.mainloop()

