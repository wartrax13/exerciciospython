'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por K
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas
um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.'''

print('HIPERMERCADO TABAJARA')
print('Tipos de carnes são:\n'
      '[1] Filé duplo\n'
      '[2] Alcatra\n'
      '[3] Picanha')

tipo = int(input('Escolha tipo da carne: '))
kg = float(input('Quantidade em Kg: '))

if tipo == 1:
    print('Você escolheu Filé duplo.')
    prestotal = kg * 5.8
    if kg > 5:
        total = kg * 5.8
        print(f'Preço a pagar: R${total} ')
        print('Sem desconto.')
    else:
        total = kg * 4.9
        print(f'Preço total: R${total}')
        print(f'O desconfoi de: R${round(prestotal - total,1)}')

elif tipo == 2:
    print('Você escolheu Alcatra.')
    prestotal = kg * 6.8
    if kg > 5:
        total = kg * 6.8
        print(f'Preço total: R${total} ')
        print('Sem desconto.')
    else:
        total = kg * 5.9
        print(f'Preço total: R${total}')
        print(f'O desconfoi de: R${round(prestotal - total,1)}')

elif tipo == 3:
    print('Você escolheu Picanha')
    prestotal = kg * 7.8
    if kg > 5:
        total = kg * 7.8
        print(f'Preço total: R${total} ')
        print('Sem desconto.')
    else:
        total = kg * 6.9
        print(f'Preço total: R${total}')
        print(f'O desconfoi de: R${round(prestotal - total,1)}')
else:
    print('Opção inválida.')
