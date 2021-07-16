'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

n = int(input('Digite um número: '))
if n % 3 == 0 or n % 2 == 0:
    print('Não é primo.')
else:
    print('É primo.')