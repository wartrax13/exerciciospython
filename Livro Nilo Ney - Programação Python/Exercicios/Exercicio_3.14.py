"""Escreva um programa para calcular a redução do tempo de tvida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos dee vida a cada cigarro, calcule quantos dias de vida um fumante perderá.
Exiba o total em dia."""

cig = int(input('How much cigarttes do you smoke for a day? '))
years = int(input('How many years ago? '))
day_min = 24 * 60
year_min = day_min * 365

year_life = year_min / 10

total = (years * year_life) / day_min
print(f'You will lose {total} days of life')
