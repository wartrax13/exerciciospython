n = 1
lista = []
while n != 0:
    n = int(input())
    for x in range(1, n + 1):
        lista.append(x)

    if n != 0:
        print(' '.join(map(str, lista)))
        lista = []
