# teniendo como entrada un numero entero, determine cuantos digitos tiene
# cuantos de ellos son pares e impares, calcule la sumatoria,
# la productoria y el promedio de estos
def num_pairs (num):
    contador = 0

    for i in range(1, num + 1):
         if num % 2 == 0:
            contador += 1
           # print("pair")
            return True
         else:
          #  print("inpair")
            return False
        
whole_number = int(input( " Enter the number  "))
def digit_number(whole_number):
    pair = 0
    inpair = 0
    summation = 0
    productive = 1
    count = 0 
    digit = 0
    
    while(whole_number!=0):
        digit=whole_number%10
        whole_number=whole_number//10   
        if num_pairs(digit): 
            pair += 1
        else: 
            inpair += 1 
        summation += digit
        productive *= digit
        count +=   1
 
    print(f"tienes {pair} numero pares")
    print(f"tienes {inpair} numeros impares")
    print(f"la sumatoria is {summation}")
    print(f"la productividad es  {productive} ")
    print(f"el promedio es  {summation / count}")

digit_number(whole_number)

     


   