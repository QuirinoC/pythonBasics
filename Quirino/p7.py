import os

value = 0
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    user_input = input(f"Add or substract (+/-): \n{value} ")

    if user_input[0] in ('+','-'):
        op = user_input[0]
        number = user_input[1:].strip()
    else:
        break
    if not number.isnumeric(): break
    if op == '+':
        value += int(number)
    elif op == '-':
        value -= int(number)
    else: 
        break
    