'''
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
'''

def reverso(n):
    q = str(n)
    return q[::-1]

print(reverso(12345))