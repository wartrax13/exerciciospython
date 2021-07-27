'''
Escreva um programa que leia dois números.
Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utiliza apenas operadores
de soma e subtração.
'''

dividendo = int(input())
divisor = int(input())
q = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    q = q + 1
resto = x
print(f'{dividendo}/{divisor} = {q} e resto = {x}')