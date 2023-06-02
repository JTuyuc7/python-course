

#^ Functions Inputs, arguments and parameters
import math
# def greet():
#     print(f'Line 1')
#     print(f'Line 2')
#     print(f'Line 3')

# greet()

# def greet1(p1, p2, p3):
#     print(f'{p1}')
#     print(f'{p2}')
#     print(f'{p3}')

# greet1('first parameter', 15, ['hello', 'from', 'the function'])
# greet1('first ', True, 'Hello')

#^ Function with more than 1 argument

# def greet2(name, *args):

#     print(f'The first parameter is {name}')
#     # print(f'This should be an object or tuple, {*args}')
#     for arg in args:
#         print(f'Each argument {arg}')

# greet2('james', arg1='firstName', arg2='lastName')

#* Excersice day 8 No.1

# def paint_calc(height, width, cover):
#     result = (height * width) / cover
#     result = math.ceil(result)
#     print(f"You'll need {result} cans of paint.")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#* Excersice day 8 No.2

# def prime_checker(number):
#     is_prime = True
#     for n in range(2, number):
#         if number % n == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
# n = int(input("Check this number: "))
# prime_checker(number=n)

#* Final project day 8 
#^ Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(len(alphabet))
# def encrypt(text, shift):
#     indexes_list = []
#     for l in text:
#         value = alphabet.index(l) + shift
#         #! Validate if the letter is close to Z
#         indexes_list.append(alphabet[value])

#     print(f"{''.join(indexes_list)}")

# def decrypt(text, shift):
#     indexes_list_decrypt = []
#     for l in text:
#         value = alphabet.index(l) - shift
#         if value < 0:
#             value = alphabet.index( len(alphabet - 1))
#         indexes_list_decrypt.append(alphabet[value])
    
#     # print(indexes_list_decrypt)
#     print(f"{''.join(indexes_list_decrypt)}")

def caesar(start_text, shift_text, cipher_direction):
    end_text = ""    
    if cipher_direction == 'decode':
            shift_text *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_text
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {cipher_direction} is {end_text}')

def ceaser_program():

    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decript \n")
        text = input('Enter the message \n').lower()
        shift = int(input('Type the shift number \n'))
        shift = shift % 26
        caesar(text, shift, direction)
        option = input('Would you like to continue? "Y" for yes, "N" for no \n').lower()
        if( option == 'N'):
            should_continue = False
            print('Goobye!!')
        # if( direction == 'encode'):
        #     encrypt(text, shift)
        # else:
        #     decrypt(text, shift)

ceaser_program()



# mjqqt