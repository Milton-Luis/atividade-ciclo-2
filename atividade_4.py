# coding: utf-8

#atividade 4 - números primos com retorno boolean

def verfica(n):
    num = 0
    for i in range(1, 100):

        if n % i == 0 or n == 1:
            num += 1

        if num == 2:
            nPrimo = True

    if num > 2:
        nPrimo = False
    return nPrimo


for j in range(2, 100):
    x = verfica(j)
    print("Nº {}: {}".format(j, x))