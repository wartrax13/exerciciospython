'''
12 1 5.30
16 2 5.10
'''

a, b, c = input().split()
d, e, f = input().split()
VALOR = (int(b) * float(c)) + (int(e) * float(f))

print('VALOR A PAGAR: R$ {:.2f}'.format(VALOR))