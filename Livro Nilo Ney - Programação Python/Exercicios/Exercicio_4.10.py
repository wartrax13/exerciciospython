"""
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir...

"""

energy = int(input('Quant kWh: '))
type = str(input('Instalation type: ')).upper()

if type == 'R':
    if energy <= 500:
        price = energy * 0.4
    else:
        price = energy * 0.65

elif type == 'C':
    if energy <= 1000:
        price = energy * 0.55
    else:
        price = energy * 0.60

elif type == 'I':
    if energy <= 5000:
        price = energy * 0.55
    else:
        price = energy * 0.60

print(f'The value is: {price}')