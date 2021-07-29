valor = float(input('Digite o valor a pagar: '))
if valor < 0.01:
    print('Não temos essa cedula.')
cedulas = 0
atual = 100.0
apagar = valor

while True:
    if valor < 0.01:
        raise('Error!')
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
        elif atual == 1:
            atual = 0.5
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05


        cedulas = 0