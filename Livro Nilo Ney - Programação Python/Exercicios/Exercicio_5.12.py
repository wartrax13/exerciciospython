"""Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mes seguinte."""

dep = 100 # int(input('Deposito inicial: '))
taxa = 5 # int(input('Taxa de juros: '))
x = 1
dep2 = dep
while x <= 24:
    dep2 += (dep2 * (taxa / 100))
    print(f' Mês {x} = R${dep2:.2f}')
    dep3 = int(input('Você deseja depositar mais? Para NÃO, digite 0 (zero): '))
    dep2 += dep3

    x += 1

print(f'Você ganhou {dep2 - dep:.2f}')