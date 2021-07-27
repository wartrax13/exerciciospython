"""
Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa,
cobrando R$5 por km acima de 80km/h
"""

vel = int(input('How fast?[km/h] '))
if vel > 80:
    mulct = 5 * (vel-80)
    print('Você foi multado.')
    print('Valor R${}.'.format(mulct))
