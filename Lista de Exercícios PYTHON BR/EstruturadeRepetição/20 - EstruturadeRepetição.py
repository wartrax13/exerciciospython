'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular
o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''
from math import factorial
n = 1
while n != 0:
    n = int(input('[Para cancelar digite 0] Digite um número: '))
    if n == 0:
        break
    x = 0
    while x < n:
        x += 1
        if x == n:
            print(f'{x} = {factorial(n)}')
        else:
            print(x, end=' x ')
print('Finalizado.')
