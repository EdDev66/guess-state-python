import pandas
import turtle

screen = turtle.Screen()
screen.title('USA States')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Guessed', prompt='What is another state name?')

    # Extract state names
    data = pandas.read_csv('50_states.csv')
    state_names_data = data.iloc[:, 0]
    state_names = state_names_data.tolist()

    # Exit and save the remaining states to a file
    if answer_state == 'Exit' or answer_state == 'exit':
        remaining_states = [x for x in state_names if x not in guessed_states]
        df = pandas.DataFrame(remaining_states)
        df.to_csv('states_to_learn.csv', index=False)
        break

    def write_state(name, x, y):
        state_name = turtle.Turtle()
        guessed_states.append(name)
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(x, y)
        state_name.write(name)

    # Check if the user's choice is a valid state
    state_names_lower = [item.lower() if isinstance(item, str) else item for item in state_names]
    print(state_names_lower)
    if answer_state.lower() not in state_names_lower:
        print('Not a state!')
    else:
        # Extract full state details
        user_state = answer_state.title()
        if user_state not in guessed_states:
            state_details = data[data['state'] == user_state]

            # Mark state on map
            state_coords_x = state_details['x'].values[0]
            state_coords_y = state_details['y'].values[0]
            write_state(user_state, state_coords_x, state_coords_y)


screen.exitonclick()


