user_input = input("Altura: ")

while user_input.isnumeric():
    height = int(user_input)
    while height > 0:
        
        print(height * "*")

        height = height - 1
        
    user_input = input("Altura: ")
