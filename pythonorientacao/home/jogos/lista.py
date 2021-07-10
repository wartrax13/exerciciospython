'''Vamos tentar resolver alguns desafios. Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,
-52] faça um programa que:
a) imprima o maior elemento
b) imprima o menor elemento
c) imprima os números pares
d) imprima o número de ocorrências do primeiro elemento da lista
e) imprima a média dos elementos
f) imprima a soma dos elementos de valor negativo'''

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]
maiorValor = lista[0]
menorValor = lista[0]
listaPares = []
ocorrenciasItem1 = 0
mediaElementos = 0
somaNegativos = 0
for index in range(0, len(lista)):
    # Maior Valor
    if maiorValor < lista[index]:
        maiorValor = lista[index]
    # Menor Valor
    if menorValor > lista[index]:
        menorValor = lista[index]
    # Números pares
    if lista[index] % 2 == 0:
        listaPares.append(lista[index])
    # Números de ocorrencias
    if lista[index] == lista[0]:
        ocorrenciasItem1 = ocorrenciasItem1 + 1
    # Média elementos
    mediaElementos =+ mediaElementos + lista[index]
    #Some dos números negativos
    if lista[index] < 0:
        somaNegativos = somaNegativos + lista[index]
mediaElementos = mediaElementos / len(lista)

print(maiorValor)
print(menorValor)
print(listaPares)
print(ocorrenciasItem1)
print(mediaElementos)
print(somaNegativos)