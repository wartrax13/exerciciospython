valor = float(input("Digite o valor a pagar:"))
cédulas = 0
atual = 100
apagar = valor
print('NOTAS:')
while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        if atual >=1:
            print("{} notas(s) de R${}".format(cédulas, atual))
        else:
            print("{} notas(s) de R${}".format(cédulas, atual))
        if apagar <= 1:
            break
        elif atual == 100:
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
            atual = 0.50
        cédulas = 0
print('MOEDAS:')
while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        if atual >= 0.01:
            print("{} moeda(s) de R${}".format(cédulas, atual))
        else:
            print("{} moeda(s) de R${}".format(cédulas, atual))
        if apagar == 0:
            break
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cédulas = 0