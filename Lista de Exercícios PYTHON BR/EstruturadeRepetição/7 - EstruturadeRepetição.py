'''Faça um programa que leia 5 números e informe o maior número.'''
x = 1
lista = []
while x <= 5:
    x += 1
    n = int(input('Digite o número: '))
    lista.append(n)
print(f'O maior número é: {max(lista)}')

