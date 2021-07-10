'''Vamos tentar resolver alguns desafios. Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,
-52] faça um programa que:
a) imprima o maior elemento
b) imprima o menor elemento
c) imprima os números pares
d) imprima o número de ocorrências do primeiro elemento da lista
e) imprima a média dos elementos
f) imprima a soma dos elementos de valor negativo'''

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]

for index in range(0, len(lista)):

print(max(lista))
print(min(lista))
print(lista[0])


if lista % 2 == 0:

    print(lista)