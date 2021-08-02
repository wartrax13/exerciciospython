n = 1
q = 0
while n <= 6:
    x = float(input())
    if x > 0:
       q += 1
    n += 1
print('{} valores positivos'.format(q))
