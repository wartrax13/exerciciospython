'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

from time import strftime

data_atual = int(strftime("%Y"))
data_inicio = 1996
anos = data_atual - data_inicio
salario_inicial = 1000
percentual = 0.015

for x in range(1,anos):
    aumento = salario_inicial * percentual
    salario_inicial += aumento
    print(f'Percentual: {percentual}')
    percentual = percentual * 2
    print(f'Salário: {round(salario_inicial)}')




