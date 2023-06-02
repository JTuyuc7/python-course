

#~ PRIMITIVE DATA TYPES PYTHON 

#! STRINGS
#? SUBSTINGS
'''
print("hellow"[0])

print('123'+'456')
'''

#? INTEGERS
num = 123456
# print(num)

#? FLOAT NUMBERS

num1 = 10.53
# print(num1)

#? BOOLEAN
val = True
# print(val)

#? How to check the type of data
# print(type(12))

#? How to cast the value of a variable
# print(str(300)) #& str is using to cast integers to strings

#* Excercice 1
# two_digit_number = input("Type a two digit number: ")

# num1 = int(two_digit_number[0])
# num2 = int(two_digit_number[1])

# print(num1 + num2)

#? ---------------------------

#? MATEMATICAL OPERATORS
'''
    PEMDAS
    - Parentheses ()
    - Exponents **
    - Multiplication *
    - Division /
    - Addition +
    - Substraction -
'''

# print(3*3+3/3-3)

#* EXCERCISE 2 of day 2

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# result = int(float(weight) / (float(height) * float(height)))

# print(result)

#? Rouding decimals
# print( round(8/3, 2))

#! Floor division
# print( 8 // 3)

#* EXERCISE 3 of day 2
# age = input("What is your current age? ")

# 1 year = 12 months
# 1 year = 52 weeks
# 1 year = 365 days

# default_age = 90

# total_weeks = (default_age - int(age)) * 52
# total_days = (default_age - int(age)) * 365
# total_months = (default_age -  int(age)) * 12

# print(f'You have {total_days} days, {total_weeks} weeks, and {total_months} months left.')

#! Discounts
#* FINAL PROJECT FOR DAY 2
print('Welcome to the tip calculator.')
amount = float(input('What was the total bill? $'))
disctount = float(input('What tip would you like to give? 10, 12, or 15? '))
people = float(input('How may people to split the bill? '))

total_tip = amount * (disctount / 100)
total_amount = amount + total_tip
total_each_person = round(total_amount / people, 2)
final_amount = "{:.2f}".format(total_each_person)

print(f'Each person should pay: ${final_amount}')