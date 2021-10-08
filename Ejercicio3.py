# De los n elementos de la serie fibonacci diga cuantos son pares, 
# cuantos impares y cuantos ceros 
a = 0 
b = 1  
n = int(input(" Enter the number of numbers you want from the fibonacci series \n "))
even = 0 
odd = 0 
cero = 0 
while n > a :  
    
    c = b + a 
    a = b
    b = c 
    if a % 2 == 0 : 
        even += 1
    else:
        odd += 1 
    if cero == 0:
       cero += 1 

print(f" The numbers pair this {even}")
print(f" The numbers impair this {odd}")
print(f" The numbers cero this {cero}")
    