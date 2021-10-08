# En 1994 el pais A tiene una poblacion de 25 millones de habitantes 
# y el pais B de 19.9 millones. las tasas de crecimiento son de 2% y 3%
# respectivamente. Desarrollar un algoritmo para informar en que año la 
# poblacion del pais B supera la del pais A.
country_A = 25  
country_B = 19.9
year = 1994 
while country_B < country_A :
    country_A = country_A * 0.02 + country_A
    country_B = country_B * 0.03 + country_B
    year += 1
    print(f'Poblacion de pais 1 {country_A }') 
    print(f'Poblacion de pais 2 {country_B}')
    print(f'año {year}')  
