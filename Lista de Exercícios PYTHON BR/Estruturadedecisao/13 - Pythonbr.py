'''Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

dias = {1: 'domingo', 2: 'segunda', 3: 'terça', 4: 'quarta', 5: 'quinta', 6: 'sexta', 7: 'sabado'}
escolha = int(input('Escolha um dia da semana, de 1 a 7: '))

print(dias[escolha])