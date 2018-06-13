user_input = input("Numero: ")
numeros = []
while user_input.isnumeric():
    numeros.append(int(user_input))
    user_input = input("Numero: ")
print(sum(numeros)/len(numeros))

def aFunction():
    pass