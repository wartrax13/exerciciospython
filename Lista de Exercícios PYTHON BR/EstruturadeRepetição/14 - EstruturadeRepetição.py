'''Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares.'''
p = 0
i = 0
for x in range(1,11):
    n = int(input('Digite o número inteiro: '))
    if n % 2 == 0:
        p += 1
    else:
        i += 1
print(f'{p} pares e {i} impares')
