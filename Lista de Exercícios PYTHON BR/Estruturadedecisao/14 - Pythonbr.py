'''
Faça um programa que lê as duas notas parciais obtidas por um aluno
numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
 e a mensagem “APROVADO” se o conceito for A, B ou C
 ou “REPROVADO” se o conceito for D ou E.
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = n1 + n2 / 2
print(f'As notas foram {n1} e {n2}.')
print(f'A média entre elas foi {media}.')
if media >= 6.0:
    print('APROVADO')
    if media < 7.5:
        print('C')
    elif 7.5 <= media < 9.0:
        print('B')
    else:
        print('A')
else:
    print('REPROVADO')
    if 4.0 <= media < 6.0:
        print('D')
    else:
        print('E')
