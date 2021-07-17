'''
Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''
nulos = [0]
branco = [0]
votos = [0]
larissa = [0]
joao = [0]
pedro = [0]
jose = [0]
print('ELEIÇÕES')
print('-----------')
print('Vote nas seguintes opções:\n'
      '[1] José\n'
      '[2] Pedro\n'
      '[3] João\n'
      '[4] Larissa\n'
      '[5] Voto nulo\n'
      '[6] Voto branco.')
c = 7
while c != 0:
    c = int(input('Vote:'))
    votos.append(c)
    if c == 6:
        branco.append(c)
    elif c == 5:
        nulos.append(c)
    elif c == 1:
        jose.append(c)
    elif c == 2:
        pedro.append(c)
    elif c == 3:
        joao.append(c)
    elif c == 4:
        larissa.append(c)
    else:
        print('Somente até a opção 6. Tente novamente.')
print(f'Foram {len(larissa)} votos para Larissa,\n'
      f'{len(pedro)} para o Pedro\n'
      f'{len(joao)} para o João\n'
      f'{len(jose)} para o José\n'
      f'{len(nulos)} Nulos\n'
      f'{len(branco)} Brancos\n'
      f'{round((len(nulos) * 100) / len(votos))}% dos votos nulos\n'
      f'{round((len(branco) * 100) / len(votos))}% dos votos brancos')


