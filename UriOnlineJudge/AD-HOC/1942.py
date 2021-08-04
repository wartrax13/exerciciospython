'''
Loteria
'''

p, n = [int(x) for x in input().split(' ')]
som_a = 0
som_b = 0
som_c = 0
lista = []
for i in range(p):
    a, b, c = [int(x) for x in input().split(' ')]
    som_a += a
    som_b += b
    som_c += c
if som_a % 2 == 0 and som_b % 2 == 0 and som_c % 2 == 0:
    par = True
elif som_a % 2 != 0 and som_b % 2 != 0 and som_c % 2 != 0:
    par = True
else:
    par = False

if par:
    print('S')
else:
    print('N')
