'''
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''
A = []
B = []
C = []
eleitores = int(input('Quantos eleitores há? '))
print('-------------------------')
for x in range(eleitores):
    voto = int(input('Qual seu voto?\n'
                     '[1] A\n'
                     '[2] B\n'
                     '[3] C\n'))
    if voto == 1:
        A.append(voto)
        print('Você votou no candidato A')
        print('-------------------------')
    elif voto == 2:
        B.append(voto)
        print('Você votou no candidato B')
        print('-------------------------')
    elif voto == 3:
        C.append(voto)
        print('Você votou no candidato C')
        print('-------------------------')
    else:
        print('Você votou errado. Perdeu.')
        print('-------------------------')
print(f'O candidato A teve {len(A)} votos\n'
      f'O candidato B teve {len(B)} votos\n'
      f'O candidato C teve {len(C)} votos')
