

# * Day 5 loops
import random
# & For in loop python
fruits = ['apple', 'orange', 'pear', 'pineaple', 'peach', 'banana']

# for fruit in fruits:
#     print(f'Each fuit is {fruit} at index')

# ^ 180 124 165 173 189 169 146
# student_heights = input("Input a list of student heights ").split()
# temp = [180, 124, 165, 173, 189, 169, 146]
# total = 0
# for n in range(0, len(temp)):
#     temp[n] = int(temp[n])
#     total += temp[n]
#     print(temp[n])

# print(round(total / int(len(temp))))

'''
    #^ Solution
    total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(average_height)
'''

student_scores = [180, 124, 165, 173, 189, 169, 146]

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score

# print(highest_score, 'Numero mas alto en la lista')


# & For in rage Python
# total_sum = 0
# for x in range(1,101):
#     # print(f'{x}')
#     total_sum += x

# print(f'Total sum is {total_sum}')

# * Excersice Day 5 No.1

# total_sum = 0

# for n in range(1, 101): #! Using the range() you can pass a third parameters which will be executed like a condition
#     if(n % 2 == 0):
#         total_sum += n

# print(f'Total sum is {total_sum}')

# * Ex Day 5 No.2

# for n in range(1,101):
#     if (n%3 == 0 and n%5 == 0):
#         print('FizzBuzz')
#     elif( n % 3 ==0):
#         print('Fizz')
#     elif(n%5 == 0):
#         print('Buzz')
#     else:
#         print(n)

# * Final project PASSWORD GENERATOR

print('Welcome to the PyPassword Generator!')

letters_input = int(input('How many letters would you like in you password? \n'))

simbols_input = int(input('How many symbols would you like? \n'))

numbers_input = int(input('How many numbers would you like? \n'))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


pass_list = []
final_pass = ''

for char in range(1, letters_input + 1):
    pass_list.append(random.choice(letters))

for n in range(1, numbers_input + 1):
    pass_list.append(random.choice(numbers))

for sim in range(1, simbols_input + 1):
    pass_list.append(random.choice(symbols))

random.shuffle(pass_list)

for l in pass_list:
    final_pass += l

print(final_pass)

# total_letters = letters_input + simbols_input + numbers_input
# random_letters = ''
# for t in range(1, total_letters + 1):
#     random_l = random.randint(0, len(letters) - 1)
#     random_n = random.randint(0, len(numbers) - 1)
#     random_s = random.randint(0, len(symbols) - 1)

#     random_letters += letters[random_l]  
#     random_letters += numbers[random_n]
#     random_letters += symbols[random_s]

# print(random_letters)