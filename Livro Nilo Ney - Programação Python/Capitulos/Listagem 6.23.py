L = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))

achou = False
x = 0
while x < len(L):
    if L[x] == p:
        achou = True
        break
    x += 1
if achou:
    print(f'{p} está na posição {x+1}')
else:
    print('Não encontrado.')