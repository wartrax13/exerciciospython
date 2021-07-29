"""
PILHA DE PRATOS
"""

prato = 5
pilha = list(range(1, prato + 1))
while True:
    print(f'Existem {len(pilha)} pratos na pilha')
    print(f'Pilha atual: {pilha}')
    print('Digite E para empilhar um novo prato')
    print('ou D para desempilhar. S para sair.')
    operacao = input('Escolha operação [E,D,S]: ').upper()
    if operacao == 'D':
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f'Prato {lavado} lavado')
        else:
            print('Pilha vazia!')
    elif operacao == 'E':
        prato += 1 # novo prato
        pilha.append(prato)
    elif operacao == 'S':
        break
    else:
        print('Operação inválida.')
