'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
 Faça um programa que gere a série até que o valor seja maior que 500.
'''
penultimo = 1
ultimo = 1
termo = 1
while termo < 501:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(termo)
