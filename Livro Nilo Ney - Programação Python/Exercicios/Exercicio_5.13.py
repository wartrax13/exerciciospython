"""Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
Pergunte também o valor mensal que será pega. Imprima o número de meses para que a dívida seja paga, o total pago
e o total de juros pago."""

dep = 1000  # int(input('Deposito inicial: '))
taxa = 3 # int(input('Taxa de juros: '))
paga = 50 # int(input('Você deseja depositar mais? Para NÃO, digite 0 (zero): '))
x = 1

while dep > 0:
    dep += dep * (taxa / 100)
    print(f' Mês {x} = R${dep:.2f}')
    # dep3 = int(input('Você deseja depositar mais? Para NÃO, digite 0 (zero): '))
    dep = dep - paga
    x += 1

print(f'{x} meses')