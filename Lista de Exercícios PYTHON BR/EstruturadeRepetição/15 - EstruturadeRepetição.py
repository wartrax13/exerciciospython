'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''
penultimo = 1
ultimo = 1
n = int(input('Digite o n-ésimo termo: '))
if (n == 1) or (n == 2):
    print('1')
else:
    for x in range(1, n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        x += 1
        print(termo)