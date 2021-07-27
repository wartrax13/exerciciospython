"""Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período."""

dep = 100 # int(input('Deposito inicial: '))
taxa = 5 # int(input('Taxa de juros: '))
x = 1
dep2 = dep
while x <= 24:
    dep2 += (dep2 * (taxa / 100))
    print(f' Mês {x} = R${dep2:.2f}')
    x += 1

print(f'Você ganhou {dep2 - dep:.2f}')
