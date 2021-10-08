# Realice un mètodo que permita calcular el 
# MCD (Maximo Comùn Divisor) entre dos numeros
aux = 0 
number_one = int(input("Please enter the first number :\n")) 
number_two = int(input(" Please enter the secund number \n:"))

while number_two != 0:
    aux = number_two
    number_two = number_one % number_two
    number_one = aux

print(number_one)
print(number_two)