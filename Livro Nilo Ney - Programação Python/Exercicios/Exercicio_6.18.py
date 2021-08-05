'''
Escreva um programa que gere um dicionáiro, onde cada chave seja um caractere, e seu valor
seja um número desse caractere encontrado em uma frase lida.
Exemplo: O rato -> ['O':1,'r':1,'a': 1, 't': 1,'o':1]
'''

palavra = 'o rato' #str(input())
for x, y in enumerate(palavra):
    print('{} : {}'.format(x,y))