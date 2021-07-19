'''Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

a = float(input('Digite um lado: '))
b = float(input('Digite um lado: '))
c = float(input('Digite um lado: '))

soma = a + b
if soma >= c:
    print('Pode ser um triângulo.')
    if a == b == c:
        print('Triângulo equilátero.')
    elif a != b != c:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles.')
else:
    print('Não pode ser um triângulo.')
