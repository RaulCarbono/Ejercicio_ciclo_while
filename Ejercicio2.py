# teniendo como entrada un numero entero, determine cuantos digitos tiene
# cuantos de ellos son pares e impares, calcule la sumatoria,
# la productoria y el promedio de estos
def num_pairs (num):
    contador = 0

    for i in range(1, num + 1):
         if num % 2 == 0:
            contador += 1
            print("pair")
            return True
         else:
            print("inpair")
            return False

pair = 0
inpair = 0
summation = 0
productive = 0
count = 0 

whole_number = int("")