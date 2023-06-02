import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'

states = '50_states.csv'

# ! Add a shape to the screen to load the blank image gift
screen.addshape(image)

# ! add it to the turtle
turtle.shape(image)


# ! Locate the coordinates for the states
# ! This function help us getting the coordinates when clicking a part of a screen using turtle
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

states_data = pandas.read_csv(states)
all_states = states_data['state'].to_list()

guessed_states = []


while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt='What\'s another '
                                                                                             'state\'s name? ').title()
    print(answer_state, 'your answer??')
    # turtle.mainloop()

    if answer_state == 'Exit':
        missing_states = [state for state in guessed_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_state_csv = {'Missing States': missing_states}
        file_missing_csv = pandas.DataFrame(missing_state_csv)
        file_missing_csv.to_csv('Missing_states.csv')
        # print(missing_states)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        single_state = states_data[states_data['state'] == answer_state]
        t.goto(float(single_state['x']), float(single_state['y']))
        t.write(answer_state)
        # t.write(single_state.state.item())
        # print(type(single_state['x']))

# screen.exitonclick()
