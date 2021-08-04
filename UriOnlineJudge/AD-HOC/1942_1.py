'''
4 3
9 4 7
4 4 4
2 7 2
2 2 1

3 3
3 2 1
6 5 4
4 4 4

2 3
1 2 3
5 6 7

'''

p, n = [int(x) for x in input().split(' ')]
par = 0
impar = 0
lista = []
for i in range(p):
    x = [int(x) for x in input().split(' ')]

    if i >= 1:
        for j in range(0, n):
            x[j] += lista[j]
    lista = x

for a in lista:
    if a % 2 == 0:
        par += 1
    else:
        impar += 1
if par == n or impar == n:
    print('S')
else:
    print('N')



