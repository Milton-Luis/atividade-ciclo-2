# coding: utf-8

# atividade 1 - idade expressa em anos, meses e dias

idadeDias = int(input("\nInforme sua idade em dias: "))


anos = (idadeDias / 365)
meses = (idadeDias % 365) / 30
dias = (idadeDias % 365) % 30


print("\nA idade da pessoa expressa em dias, meses e anos é: \n%d ano(s), %d mes(es) e %d dia(s)" % (anos, meses, dias))