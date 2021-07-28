'''
Leia um valor inteiro.
A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
'''

valor = int(input())
print(valor)

cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedula in cedulas:
    qt_cedulas = int(valor / cedula)
    # imprime a quantidade de cedulas
    print('{} nota(s) de R$ {},00'.format(qt_cedulas, cedula))
    valor -= qt_cedulas * cedula
