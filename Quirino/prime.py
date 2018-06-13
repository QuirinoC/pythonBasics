from math import sqrt
number = int(input("n: "))
for i in range(2, number):
	if number % i == 0:
		print("not prime"); break
else:
	print("prime")
