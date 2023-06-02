

#& Function with outputs

# def format_name(f_name, l_name):
#     return f'{f_name.title()} {l_name.title()}'

# final_name = format_name('james', 'tuyuc')

# print(final_name)

#* Final Project Day 10 - Calculator

def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if( a == 0):
        return 'You can not divide by 0'
    else:
        return a / b
    
operations = {'+': add, '-': substract, '*': multiply, '/': divide }

def show_operations(operators):
    for op in operators:
        print(op)

def calculator():
    should_continue = True
    num1 = float(input('What is the first number? \n'))

    while should_continue:
        show_operations(operations)
        operation_symbol = input('Select an option to operate with \n')
        function_selected = operations[operation_symbol]    
        num2 = float(input('What is the next number? \n'))

        answer = function_selected(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        more_operations = input(f'Do you want to continue calculate with {answer} [Y] for "Yes", [S] to start again: \n').lower()
        print(more_operations, 'value of selection')
        if more_operations == 'y':
            num1 = answer
        elif more_operations == 's':
            should_continue = False
            calculator()
        else:
            should_continue = False

calculator()