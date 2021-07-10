def divisao(a, b):
    return a / b

def velocidade_media(distancia, tempo):
    a = divisao(distancia, tempo)
    return a


def calculadora(a, b):
    soma = a + b
    sub = a - b
    mult = a * b
    div = a / b
    return soma, sub, mult, div

print(velocidade_media(100, 20))

print(calculadora(10,5))