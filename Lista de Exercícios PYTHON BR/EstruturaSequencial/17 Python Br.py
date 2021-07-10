''' Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.'''

print('Loja de Tintas! Bem vindo!')
print('--'*20)

tamanho = int(input('Qual o tamanho da parede [m2]? '))
litro = tamanho / 6
if litro <= 18:
    galoes = litro / 3.6 + 1
    print(f'São necessários {galoes:.0f} galões.')
else:
    quant = litro / 18
    total = quant - int(quant)
    galoes = (total * 18) / 3.6 + 1
    print(f'É necessário {int(quant)} latas.')
    print(f'E {galoes:.0f} galões')



#print(f'Você irá precisar de {quant:.2f} latas')
#print(f'Total é {total:.2f}')