

# #* Namespaces Local vs Global Scopes

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f'Enemies inside function {enemies}')

# increase_enemies()

# print(f'enemies outside function {enemies}')


# # todo How use global variables and change inside a function
# enemies1 = 0
# def increase_enemies1():
#     global enemies1
#     enemies1 += 0
#     print(f'Enemies inside function: {enemies1}')

# increase_enemies1()

# print(f'Enemies outside function: {enemies1}')

# #* Declare constants variables in python
# #* Use CAPITALIZE LETTERS TO DEFINE IT

# PI = 3.141516

#~ Final Excersice Day 12
import random
attempts = 0
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
guess_number = random.choice(number_list)
should_continue = True
counter = 0

print(f'for testing the number is {guess_number}')

print('Welcome to the guess number game')
print('Computer will choose a number between 1 - 100')
difficulty = input("Choose the level of game [e] for 'easy', [d] for 'difficult': \n").lower()

if difficulty == 'e':
    attempts = 10
elif difficulty == 'd':
    attempts = 5

attempts -= 1
# print(attempts, counter, 'dificultad')

while attempts > 0 and should_continue:
    # print('hola desde el while')
    guess = int(input(f'Make a guess: \n'))

    if guess == guess_number:
        should_continue = False
        print(f'You won, congrats')

    elif guess > guess_number:
        print(f'To high, try again, you have {attempts} attempts left.')
    attempts -= 1