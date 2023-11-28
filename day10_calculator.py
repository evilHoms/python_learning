def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def dev(a, b):
    return a / b

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": dev,
}
def calculator():
    first_num = float(input('Enter first number: '))

    while True:
        operator = input('Enter operator (+, -, *, /): ')
        second_num = float(input('Enter second number: '))
        
        method = operators[operator]
        
        result = method(first_num, second_num)
        print(f'{first_num} {operator} {second_num} = {result}')
        
        if input(f'Wanna continue with {result}? (y / n): ') == 'n':
            calculator()
        
        first_num = result
        
calculator()