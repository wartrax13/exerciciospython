'''
Escreva um programa para controlar uma pequena máquina registradora.
'''

soma = 0
x = 1
while x != 0:
    x = int(input('Digite o código: '))
    if x == 0:
        break
    qt = int(input('Digite a quantidade: '))
    soma1 = 0
    if x == 1:
        soma1 = 0.5 * qt
        soma += soma1
    elif x == 2:
        soma1 = 1 * qt
        soma += soma1
    elif x == 3:
        soma1 = 4 * qt
        soma += soma1
    elif x == 5:
        soma1 = 7 * qt
        soma += soma1
    elif x == 9:
        soma1 = 8 * qt
        soma += soma1
    elif x == 0:
        break
    else:
        print('Codigo inválido. Tente novamente.')


print('Obrigado!')
print('Total da compra foi R${:.2f}'.format(soma))

