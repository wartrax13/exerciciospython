'''
Altere o programa de cálculo dos números primos,
informando, caso o número não seja primo, por quais número ele é divisível.
'''

n = int(input('Digite um número: '))
if n % 3 == 0:
    print('Não é primo. É divisivel por 3.')
elif n % 2 == 0:
    print('Não é primo. É divisível por 2.')
else:
    print('É primo.')