'''As Organizações Tabajara resolveram dar um aumento de salário
aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o
reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''
salario = int(input('Qual o seu salário? '))
if salario <= 280:
    print(f'Seu salário atual é de R${salario}')
    print(f'Você terá um aumento de 20%. Valor do aumento: R${salario * 0.20}')
    print(f'Portanto irá receber R${salario * 1.2}.')
elif salario < 700:
    print(f'Seu salário atual é de R${salario}')
    print(f'Você terá um aumento de 15%. Valor do aumento: R${salario * 0.15}')
    print(f'Portanto irá receber R${salario * 1.15}.')
elif salario < 1500:
    print(f'Seu salário atual é de R${salario}')
    print(f'Você terá um aumento de 10%. Valor do aumento: R${salario * 0.1}')
    print(f'Portanto irá receber R${salario * 1.10}.')
else:
    print(f'Seu salário atual é de R${salario}')
    print(f'Você terá um aumento de 5%. Valor do aumento: R${salario * 0.05}')
    print(f'Portanto irá receber R${salario * 1.05}.')