'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

x = 0
lista = []
while x < 5:
    x += 1
    n = int(input('Digite o número: '))
    lista.append(n)
print(f'A soma dos números é: {sum(lista)}')
print(f'A média é {sum(lista) / x} ')