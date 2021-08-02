'''
Como um horário "próximo a meia noite" pode ser tanto alguns minutos antes quanto alguns minutos depois,
Toguro pediu a sua ajuda para criar um algoritmo que dado o valor M de minutos para ser
considerado antes e depois da meia noite, o nome do morador e o horário do suposto avistamento,
mostrasse de forma ordenada pelo horário os avistamentos que podem ser catalogados como relatos verdadeiros.
'''

a, b = [int(x) for x in input().split(' ')]
lista = []
c = []
while b > 0:
    h, n = [h.strip() for h in input().split()]

    if int(h[3:]) >= 45:
        c.append(int(h[3:]))
        c.sort()

        if int(h[3:]) < c[0]:
            lista.insert(0, n)
        else:
            lista.append(n)

    elif int(h[3:]) <= 15:
        c.append(int(h[3:]))
        c.sort()
        if int(h[3:]) < c[0]:
            lista.insert(0, n)
        else:
            lista.append(n)

    b -= 1

for i in lista:
    print(i)
