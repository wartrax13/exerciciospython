'''
Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
'''

escolha = 1
while escolha != 0:
    print('---- Menu ----')
    print('[1] Adição \n'
          '[2] Subtração \n'
          '[3] Divisão \n'
          '[4] Multiplicação\n'
          '[0] Sair')
    escolha = int(input('Sua escolha: '))
    if escolha > 4:
        print('Não existe essa opção.')
    n = 1
    x = 1
    if escolha == 1:
        print('Soma')
        while n <= 10:
            print(f'{x} + {n} = {x + n}')
            n += 1
    if escolha == 2:
        print('Subtração')
        while n <= 10:
            print(f'{x} - {n} = {x - n}')
            n += 1
    if escolha == 3:
        print('Divisão')
        while n <= 10:
            print(f'{x} % {n} = {x / n}')
            n += 1
    if escolha == 4:
        print('Multiplicação')
        while n <= 10:
            print(f'{x} x {n} = {x * n}')
            n += 1
print('Obrigado!')