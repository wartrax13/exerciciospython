'''
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.

'''
students = 0
amount = int(input('Quantas turmas? '))
soma = []
for x in range(1, amount+1):
    students = int(input(f'Quantos estudantes para {x}ª turma? '))
    if students <= 40:
        soma.append(students)
print(f'São {amount} turmas')
print(f'São {sum(soma)} alunos em todas as turmas')
print(f'A média de alunos por turma é de {sum(soma) / amount} alunos')

