"""Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, de 15% """

wage = int(input('Enter your salary: '))
if wage < 1250:
    wage_increased = wage + (wage * 0.15)

elif wage >= 1250:
    wage_increased = wage + (wage * 0.10)

print(f'Your wage is R${wage_increased:.2f} now')