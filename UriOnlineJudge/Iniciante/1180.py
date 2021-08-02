N = int(input())


X = list(input().split())
minimo = min(X)
print('Menor valor: {}'.format(minimo))
print('Posicao: {}'.format(X.index(minimo)))