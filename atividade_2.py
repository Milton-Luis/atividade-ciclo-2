#coding: utf-8

#atividade 2 - area do triangulo

a = int(input("1º: "))
b = int(input("2º: "))
c = int(input("3º: "))


if (a > b+c):
    print("não forma triangulo \nValores Lidos {}, {}, {}". format(a, b,c))

else:
    area = int((a*b)/2)
    print("Área: {}".format(area))