# De n numeros primos contenidos en un intervalo  (por ejemplo los numeros
# primos del 1 al 100), calcule la sumatoria, la productoria y el promedio.
def is_prime(num):
    contador = 0

    for i in range(1, num + 1):
        if i == 1 or i == num:
            continue
        if num % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

summation = 0
productive = 1
count = 0

interval_1 = int(input("Please, enter the firts number the inverval: \n"))
interval_2 = int(input("Please, enter the secund number the interval: \n"))


while interval_1 <= interval_2:
    if  is_prime(interval_1):
        summation += interval_1
        productive *= interval_1
        count += 1
    interval_1 += 1

print(f"The summation the interval is : {summation}")
print(f"The productive the interval is : {productive}")
print(f"the average the interval is: {summation / count}")