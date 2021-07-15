'''Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados.
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

print('Loja de Tintas! Bem vindo!')
print('--'*20)

tamanho = int(input('Qual o tamanho da parede [m2]? '))
litro = tamanho / 3
if litro > 18:
    quant = round(litro / 18)
    total = quant * 80

    print(f'Você irá precisar de {quant:.2f} latas')
    print(f'Total é {total:.2f}')

else:
    print('Você necessita apenas de uma lata. O total é de R$80,00')