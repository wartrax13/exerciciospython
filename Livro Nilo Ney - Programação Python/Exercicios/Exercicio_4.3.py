"""Escreva um programa que leia três números e que imprima o maior e o menor"""

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

if a > b and a > c:
    print('A é o maior.')
elif c > a and b:
    print('C é o maior')
elif b > a and b > c:
    print('B é o maior')
