lista = [15, 7, 27, 39]
p = int(input('Procura um número: '))
v = int(input('Procura um número 2: '))
x = 0

while x < len(lista):
    if lista[x] == p:
        break
    else:
        if lista[x] == v:
            print(f'{v} foi encontrado na {x+1} posição.')
            break
    x += 1
if x < len(lista):
    if p in lista:
        print(f'{p} Achado em {x+1}')
    elif v in lista:
        print(f'{v} achado em {x+1}')
else:
    print(f'{p} não encontrado.')