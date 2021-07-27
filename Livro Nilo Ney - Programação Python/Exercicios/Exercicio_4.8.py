"""
Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação.
"""

a = int(input('Enter your number: '))
b = int(input('Enter your number: '))
op = str(input('Qual operação [+, -, *, /: '))
if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
else:
    print('Operação inválida.')
