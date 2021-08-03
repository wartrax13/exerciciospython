'''
Jornada nas Estrelas
8
1 3 5 7 11 13 17 19
'''

x = int(input())
lista = [int(x) for x in input().split(' ')]
z = 0
soma = []
for i in lista:
    if i % 2 != 0:
        z += 1
print(z)
print(sum(lista) - z)
