

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159
e = (a * c) / 2
f = pi * (c ** 2)
g = (a + b) * c / 2
h = b * b
i = a * b

print('TRIANGULO: {:.3f}'.format(e))
print('CIRCULO: {:.3f}'.format(f))
print('TRAPEZIO: {:.3f}'.format(g))
print('QUADRADO: {:.3f}'.format(h))
print('RETANGULO: {:.3f}'.format(i))