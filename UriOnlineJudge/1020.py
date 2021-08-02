x = int(input())
m = 0
a = 0
d = 0
while x > 0:
    if x >= 365:
        x = x - 365
        a += 1
    elif x >= 30:
        x = x - 30
        m += 1
    else:
        x = x - 1
        d += 1
print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))
