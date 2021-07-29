'''
Escreva um programa que leia um numero e verifique se é ou não um número primo.
Para fazer essa verificação, calcule o resto da divisão do número por 2
e depois por todos os numeros impares até o numero lido. Se o resto de uma dessas divisões for igual a zero,
o numero não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
'''

n = int(input('Digite o valor: '))
if n < 0:
    print('Numero invalido.')
if n == 0 or n == 1:
    print('Não rola.')

else:
    if n == 2:
        print('2 é primo.')
    elif n % 2 == 0:
        print('Não é primo.')
    else:
        x = 3
        while x < n:
            if n % x == 0:
                break
        if x == n:
            print('É primo')
        else:
            print('Não é primo.')


