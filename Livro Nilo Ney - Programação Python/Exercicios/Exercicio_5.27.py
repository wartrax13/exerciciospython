'''
Escreva um programa que verifique se um número é palindromo.
Um número é palindromo se continua o mesmo caso seus dígitos sejam invertidos.
'''

n = int(input('Digite:'))
q = str(n)


if int(q[::-1]) == n:
    print('É um palindromo.')
else:
    print('Não é.')