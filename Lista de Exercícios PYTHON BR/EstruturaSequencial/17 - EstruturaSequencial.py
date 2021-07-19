''' Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

print('Loja de Tintas! Bem vindo!')
print('--' * 20)

tamanho = float(input('Qual o tamanho da parede [m2]? '))
litro = tamanho / 6
if litro <= 18:
    galoes = round(litro / 3.6 + 0.5)
    print(f'São necessários {galoes} galões.')
else:
    quant = litro / 18
    total = quant - int(quant)
    galoes = (total * 18) / 3.6
    print(f'É necessário {int(quant)} latas.')
    print(f'E {galoes:.0f} galões')

# print(f'Você irá precisar de {quant:.2f} latas')
# print(f'Total é {total:.2f}')
