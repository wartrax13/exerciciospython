'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a- Álcool:
b- até 20 litros, desconto de 3% por litro
c- acima de 20 litros, desconto de 5% por litro
d- Gasolina:
e- até 20 litros, desconto de 4% por litro
f- acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que
leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''
litros = int(input('Quantos livros pretende comprar? '))
tipo = str(input('Qual o tipo de combustível? [A] alcool ou [G] gasolina: ')).upper()
if litros <= 20 and tipo == 'A':
    print('Você obteve 3% de desconto.')
    print(f'Total: {litros * 0.97}')
elif litros <= 20 and tipo == 'G':
    print('Você obteve 4% de desconto.')
    print(f'Total: {litros * 0.96}')
elif litros > 20 and tipo == 'A':
    print('Você obteve 5% de desconto.')
    print(f'Total: {litros * 0.95}')
elif litros > 20 and tipo == 'G':
    print('Você obteve 6% de desconto.')
    print(f'Total: {litros * 0.94}')


