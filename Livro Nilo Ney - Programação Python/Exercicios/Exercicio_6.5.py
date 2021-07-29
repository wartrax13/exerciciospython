ultimo = 10
fila = list(range(1, ultimo + 1))
fila2 = list(range(1, ultimo + 1))
while True:
    print(f'Existe {len(fila)} clientes na fila.')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente no fim da fila,')
    print('ou A para realizar o atendimento, S para sair.')
    operacao = input('Operação [F, A ou S]: ').upper()
    x = 0
    sair = False
    while x < len(operacao):
        if operacao [x] == 'A':
            if (len(fila)) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} atendido.')
            else:
                print('Fila vazia!')
        elif operacao[x] == 'F':
            ultimo+=1 # incredmenta o ticket do novo Cliente
            fila.append(ultimo)
        elif operacao[x] == 'S':
            sair = True
            break
        else:
            print('Opção invalida!')
        x = x + 1
    if sair:
        break
