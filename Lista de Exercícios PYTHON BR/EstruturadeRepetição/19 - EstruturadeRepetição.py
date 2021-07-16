'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

lista = []
for x in range(0,3):
    n = int(input('Numeros: '))
    if n > 1000:
        print('Numero invalido, tente de novamente.')
    else:
        lista.append(n)

print(sum(lista))
print(max(lista))
print(min(lista))