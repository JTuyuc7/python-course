

# * DAY 3 CONDITIONALS OPERATORS IN PYTHON

# * Excercise day 3 No.1
# number = int(input("Which number do you want to check? "))

# if(number % 2):
#     print('This is an odd number.')
# else:
#     print('This is an even number.')

#! Nested conditions

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")

#* Excersice day 3 No.2 leap year

# Leap year

# 2400 Should be a leap year
# 1989 Should not be a leap year

# year = int(input('Enter a year: '))

# if(year % 4 == 0):
#     if(year % 100 == 0):
#         if( year % 400 == 0):
#             print('Leap year')
#         else:
#             print('Not leap year')
#     else:
#         print('Leap year')
# else:
#     print('Not a leap year') 

#! Multiple conditions
'''
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_pizza = 15 # 2 1
medium_pizza = 20 # 3 1
large_pizza = 25

total_bill = 0

if( size == 'S'):
    total_bill += small_pizza
    if( add_pepperoni == 'Y'):
        total_bill += 2
        if(extra_cheese == 'Y'):
            total_bill += 1
            print(f'Your final bill is: {total_bill}')
        else:
            print(f'Your final bill is: {total_bill}')
    elif(add_pepperoni == 'N'):
        if(extra_cheese == 'Y'):
            total_bill += 1
            print(f'Your final bill is: {total_bill}')
        else:
            print(f'Your final bill is: {total_bill}')
if( size == 'M'):
    total_bill += medium_pizza
    if( add_pepperoni == 'Y'):
        total_bill += 3
        if(extra_cheese == 'Y'):
            total_bill += 1
            print(f'Your final bill is: {total_bill}')
        else:
            print(f'Your final bill is: {total_bill}')
    else:
        if(extra_cheese == 'Y'):
            total_bill += 1
        else:
            print(f'Your final bill is: {total_bill}')

if( size == 'L'):
    total_bill += large_pizza
    if( add_pepperoni == 'Y'):
        total_bill += 3
        if(extra_cheese == 'Y'):
            total_bill += 1
            print(f'Your final bill is: {total_bill}')
        else:
            print(f'Your final bill is: {total_bill}')
    else:
        print('Aca')
        if(extra_cheese == 'Y'):
            total_bill += 1
            print(f'Your final bill is: {total_bill}')
        else:
            print(f'Your final bill is: {total_bill}')

'''

#! Multiple conditions on the same line

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# full_name = name1 + name2
# full_name = full_name.lower()
# # Occurs
# t = full_name.count('t')
# r = full_name.count('r')
# u = full_name.count('u')
# e = full_name.count('e')

# l = full_name.count('l')
# o = full_name.count('o')
# v = full_name.count('v')
# e = full_name.count('e')

# true = t + r + u + e
# love = l + o + v + e

# final = str(true) + str(love)
# print(final)

# if(int(final) < 10 or int(final) > 90):
#     print(f'Your score is {str(final)}, you go together like coke and mentos.')

# elif(int(final) >= 40 and int(final) <= 50):
#     print(f'Your score is {str(final)}, you are alright together.')
# else:
#     print(f'Your score is {str(final)}.')

#* FINAL EXCERSICE DAY 3

choice1 = input('Enter an option, "left" or "right" ').lower()

if choice1 == 'left':
    choice2 = input('Enter an option "wait" or "swim" ').lower()
    if choice2 == 'wait':
        choice3 = input('coose a door color, red, yellow, blue ').lower()
        if choice3 == 'red':
            print('game over')
        elif choice3 == 'yellow':
            print('You win')
        elif choice3 == 'blue':
            print('Game over')
        else:
            print('game over')
    else:
        print('game over')     
else:
    print('terminated')