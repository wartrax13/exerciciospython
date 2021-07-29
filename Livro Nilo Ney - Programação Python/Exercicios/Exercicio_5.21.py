'''
Reescreva o programa da listagem 5.14 de forma a continuar executando até que o valor digitado seja 0.
Utilize repetições aninhadas.
'''
valor = 1
while valor != 0:
    valor = float(input('Digite o valor a pagar: '))
    print('Obrigado.')
    cedulas = 0
    atual = 100.0
    apagar = valor

    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
        else:
            print('{} cédulas de R${}'.format(cedulas, atual))
            if apagar == 0:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1

            cedulas = 0
