'''
Faça um programa que simule um lançamento de dados.
Lance o dado 100 vezes e armazene os resultados em um vetor.
Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios,
 simulando os lançamentos dos dados
'''
from random import randint
lista = []
for x in range(1,101):
    dado = randint(1,6)
    lista.append(dado)
print(lista)
print(f'O número 1 apareceu {lista.count(1)} vezes')
print(f'O número 2 apareceu {lista.count(2)} vezes')
print(f'O número 3 apareceu {lista.count(3)} vezes')
print(f'O número 4 apareceu {lista.count(4)} vezes')
print(f'O número 5 apareceu {lista.count(5)} vezes')
print(f'O número 6 apareceu {lista.count(6)} vezes')

