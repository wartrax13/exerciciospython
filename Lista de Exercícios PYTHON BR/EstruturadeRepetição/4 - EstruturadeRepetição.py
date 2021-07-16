'''Supondo que a população de um país A seja da ordem de 80000 habitantes
 com uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários
para que a população do país A ultrapasse ou iguale a população do país B,
 mantidas as taxas de crescimento.'''


A = 80000
cresA = 3
B = 200000
cresB = 1.5
anos = 0
while A < B:
    anos += 1
    acresA = (A * cresA / 100)
    A = A + acresA
    acresB = (B * cresB / 100)
    B = B + acresB
    print(f'Ano {anos}')
    print(f'Cidade A: {round(A)}')
    print(f'Cidade B: {round(B)}')
    print('---------------------')

print(f'Em {anos} anos')





