compras = []
while True:
    produto = input('Produto: ')
    if produto == 'Fim':
        break
    compras.append(produto)
for p in compras:
    print(p)