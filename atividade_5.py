# coding: utf-8

# atividade 5 inversão de palavras e letras


def inverteFrase(f):
    return f[::-1]


def frase(f="The answer, my friend, is blowin' in the wind"):
    return f


s = frase()

print("Frase normal: \n{}\n ".format(s))

print("Frase com palavras e letras invertidas: \n{} ".format(inverteFrase(s)))
