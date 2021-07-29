"""
Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
"""

a = []
b = []
while True:
    x = int(input('Digite um número: '))
    if x == 0:
        break
    a.append(x)
while True:
    x = int(input('Digite um numero: [zero para parar]'))
    if x == 0:
        break
    b.append(x)

c = []

duas_listas = a[:]
duas_listas.extend(b)
x = 0
while x < len(duas_listas):
    y = 0
    while y < len(c):
        if duas_listas[x] == c[y]:
            break
        y = y + 1
    if y == len(c):
        c.append(duas_listas[x])
    x = x + 1
x = 0
while x < len(c):
    print(f'{c[x]}', end= ' ')
    x = x + 1
