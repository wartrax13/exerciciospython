p = 0
imp = 0
par = 0
neg = 0
for i in range(5):
    x = int(input())
    if x % 2 == 0:
        par += 1
    if x > 0:
        p += 1
    if x < 0:
        neg += 1
    if x % 2 != 0:
        imp += 1

print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(imp))
print('{} valor(es) positivo(s)'.format(p))
print('{} valor(es) negativo(s)'.format(neg))
