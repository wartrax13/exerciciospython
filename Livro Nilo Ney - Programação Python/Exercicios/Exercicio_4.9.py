"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o
valor da casa a comprar dividido pelo número de meses a pagar.
"""

value = int(input('What is the value? '))
wage = float(input('Your wage? '))
year = int(input('How much years? '))

years = value / (12 * (wage * 0.30))
pres = value /(years * 12)
if year < years:
    print('Você não pode comprar.')
elif year > years:
    print(f'You will pay R${pres:.2f} a month.')