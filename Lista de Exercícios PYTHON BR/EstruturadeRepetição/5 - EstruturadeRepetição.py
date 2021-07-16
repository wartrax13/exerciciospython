'''Altere o programa anterior permitindo ao usuário informar as populações
e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.'''

print('Em quanto tempo a população da cidade A se igualará a B?')

x = str(input('Quer começar? [S/N] ')).upper()
cresA = 3
B = 200000
cresB = 1.5
anos = 0
while x == 'S':
    A = int(input('Digite os habitantes da cidade A: '))
    cA = float(input('Digite o crescimento de A anual  em % (sem o símbolo): '))
    B = int(input('Digite os habitantes da cidade B: '))
    cB = float(input('Digite o crescimento de B anual em % (sem o símbolo): '))
    while A < B:
        anos += 1
        acresA = (A * cA / 100)
        A = A + acresA
        acresB = (B * cB / 100)
        B = B + acresB
        print(f'Ano {anos}')
        print(f'Cidade A: {round(A)}')
        print(f'Cidade B: {round(B)}')
        print('---------------------')
    print(f'A quantidade de habitas da cidade A se igualaria a B em {anos} anos')
    x = str(input('Deseja continuar? [S/N]')).upper()
    while x != 'N' and x != 'S':
        print('Escolha inválida. [S] para sim, [N] para não.')
        x = str(input('Deseja continuar? [S/N]')).upper()

print('Você encerrou o calculo. Até logo!')


