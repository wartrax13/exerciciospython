'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''
from math import factorial
n = int(input('Digite um número: '))
x = 0
while x < n:
    x += 1
    print(x, end=' x ')

print(f'= {factorial(n)}')