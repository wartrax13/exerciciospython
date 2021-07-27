"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até de 200 km,
e R$0,45 para viagens mais longas.
"""

distance = int(input('How far is it? '))
if distance <= 200:
    price = distance * 0.5
    print(f'The price is R${price:.2f}')
else:
    price = distance * 0.45
    print(f'The price is R${price:.2f}')
