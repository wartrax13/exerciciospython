s = 0
n = 0
while s != 5:
    x = int(input())
    if x % 2 == 0:
        n += 1
    s += 1
print('{} valores pares'.format(n))