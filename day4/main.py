

# ~ DAY 4 RANDOMISATION IN PYTHON

import random

# ? Random integers
rand_num = random.randint(0, 50)
# print(rand_num)

# ? Random floats numbers
rand_float = random.random()
# print(rand_float)

# ? Random decimal within 0, 5

num1 = random.randint(1, 4)
num2 = random.random()
# print(num1 + num2)

# * Excersice day 4 No.1
integer_rand = random.randint(0, 1)

# if(integer_rand == 1):
#     print('Heads')
# else:
#     print('Tails')


# & LISTS ON PYTHON
states_ameria = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                    "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# states_ameria.sort()
# # print(states_ameria)


# #* Excercise day 4 NO.1
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# rand_num = random.randint(0, len(names))

# print(f'Person who will pay the bill is {names[rand_num]}')


# #* Excercise day 4 NO.2
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# horizontal = int(position[0])
# vertical = int(position[1])

# map[vertical - 1][horizontal - 1] = "X"


# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

#* FINAL EXCERCISE DAY 4

human_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 from Scissors \n'))
machine_choice = random.randint(0,2)
data = ['Rock', 'Paper', 'Scissors']

#^ Piedra[0] le gana a tijeras[2]
#^ Tijeras[2] le gana a papel[1]
#^ Papel[1] vence a piedra[0]

if (human_choice == machine_choice):
    print(f'Your choice {data[human_choice]}')
    print('No one wins /*/*/*/*/*/*/*/*/*/')
    print(f'Machine choose {data[machine_choice]}')
elif(human_choice == 0 and machine_choice == 1):
    print(f'Your choice {data[human_choice]}')
    print('Machine wins')
    print(f'Machine choose {data[machine_choice]}')
elif (human_choice == 1 and machine_choice == 0):
    print(f'Your choice {data[human_choice]}')
    print('You win')
    print(f'Machine choose {data[machine_choice]}')
elif( human_choice == 2 and machine_choice == 0):
    print(f'Your choice {data[human_choice]}')
    print('Machine wins')
    print(f'Machine choose {data[machine_choice]}')
elif (human_choice == 2  and machine_choice == 1):
    print(f'Your choice {data[human_choice]}')
    print('You win')
    print(f'Machine choose {data[machine_choice]}')