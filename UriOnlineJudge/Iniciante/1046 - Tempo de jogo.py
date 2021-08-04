'''O JOGO DUROU 10 HORA(S)'''
a, b  = input().split()
a = int(a)
b = int(b)
time = 0
if a == b:
    time = 24
if a > b:
    time = (24 - a) + b
if a < b:
    time = b - a

print('O JOGO DUROU {} HORA(S)'.format(time))