'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:'''


quant = float(input('Quanto você ganha por hora? '))
horas = float(input('Quanto você trabalha por mês? '))
salariototal = quant * horas
print(f'Salario é {salariototal}')
salario1 = salariototal * 0.76
ipr = salariototal * 0.11
inss = salariototal * 0.08
sindicato = salariototal * 0.05
print(f'Seu salário é de R${salario1}')
print(f'Pagou R${ipr} de imposto de renda, R${inss} de INSS e R${sindicato} para o sindicado.')