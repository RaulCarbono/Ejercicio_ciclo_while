# teniendo como entrada un numero entero, determine cuantos digitos tiene
# cuantos de ellos son pares e impares, calcule la sumatoria,
# la productoria y el promedio de estos
        
whole_number = int(input( " Enter the number  "))
def digit_number(whole_number):
    even = 0
    odd = 0
    summation = 0
    productive = 1
    count = 0 
    digit = 0
    
    while(whole_number!=0):
        digit=whole_number%10
        whole_number=whole_number//10   
        if digit % 2 == 0:
            even += 1
        else: 
            odd += 1 
        summation += digit
        productive *= digit
        count +=   1
 
    print(f"tienes {even} numero pares")
    print(f"tienes {odd} numeros impares")
    print(f"la sumatoria is {summation}")
    print(f"la productividad es  {productive} ")
    print(f"el promedio es  {summation / count}")

digit_number(whole_number)

     


   