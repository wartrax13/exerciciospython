'''
Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.
'''
lista = []
for x in range(0,3):
    n = int(input('Numeros: '))
    lista.append(n)

print(sum(lista))
print(max(lista))
print(min(lista))