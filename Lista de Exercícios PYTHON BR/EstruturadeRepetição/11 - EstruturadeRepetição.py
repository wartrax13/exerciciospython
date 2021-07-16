'''Altere o programa anterior para mostrar no final a soma dos números.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
lista = []
for x in range(n1+1, n2):
    lista.append(x)
print(sum(lista))