"""
Números inteiros até que o usuario aperte zero.
"""

while True:
    x = int(input('Digite um número: '))
    print(x)
    if x == 0:
        break
print('Fim')