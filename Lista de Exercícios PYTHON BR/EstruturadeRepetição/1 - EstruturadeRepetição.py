'''Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.'''

nota=float(input("Enter a number from 0 to 10: "))
while (nota>10) or (nota<0):
    print('Invalid number. Try again.')
    nota=float(input("Enter a number from 0 to 10: "))


print('Valid number.')