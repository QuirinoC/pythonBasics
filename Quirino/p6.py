'''user_input = input("Numero: ")
numeros = []
while user_input.isnumeric():
    numeros.append(int(user_input))
    user_input = input("Numero: ")
print(sum(numeros)/len(numeros))

def aFunction():
    pass

'''
class Avg:
    def __init__(self):
        self.numbers = []
    def get_avg(self):
        return sum(self.numbers) / len(self.numbers)

my_avg = Avg()
while True: 
    number = input("Number: ")
    if not number.isnumeric(): break;
    my_avg.numbers.append(int(number))

print(f'Average is: {my_avg.get_avg()}')