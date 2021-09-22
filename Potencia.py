#escribe las potencias desde el 1 hasta el 1000

def run():
    LIMIT = 100000
    cont = 0
    pote_2 = 2**cont
    while pote_2 < LIMIT:
        print(f'2 elevado a {cont} es igual a :{pote_2}')
        cont +=1
        pote_2 =2**cont

run()

if __name__ == ' __main__ ':
    run()