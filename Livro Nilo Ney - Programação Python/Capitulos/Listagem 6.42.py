produto1 = ['maca', 10, 0.30]
produto2 = ['pera', 5, 0.75]
produto3 = ['kiwi', 4, 0.98]
compras = [produto1, produto2, produto3]
for e in compras:
    print('Produto: %s' % e[0])
    print('Quantidade: %d' % e[1])
    print('Preço: %5.2f' % e[2])
    