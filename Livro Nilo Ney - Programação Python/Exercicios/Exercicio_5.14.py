"""
Números inteiros até que o usuario aperte zero.
"""
soma = 0
n = 0
while True:
    x = int(input('Digite um número: '))
    if x == 0:
        break
    soma += x
    n += 1

print('Quantidade: {}'.format(n))
print('Soma: {}'.format(soma))
print('Média: {:.0f}'.format(soma/n))
print('Fim')