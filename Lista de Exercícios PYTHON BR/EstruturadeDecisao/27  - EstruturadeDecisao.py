''' Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos
e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. '''

kgmo = float(input('Quantos kg de morangos deseja? '))
kgma = float(input('Quantos kg de maçã deseja? '))
if kgmo > 5 and kgma > 5:
    totalmo = kgmo * 2.2
    totalma = kgma * 1.5
elif kgmo > 5 and kgma < 5:
    totalmo = kgmo * 2.2
    totalma = kgma * 1.8
elif kgma > 5 and kgmo < 5:
    totalmo = kgmo * 2.2
    totalma = kgma * 1.5
else:
    totalmo = kgmo * 2.5
    totalma = kgma * 1.8

totalkg = kgmo + kgma
total = totalmo + totalma
print(f'Valor normal total para {kgmo}kg de morango e {kgma}kg de maçã é de R${total}')
if total > 25 or totalkg > 8:
    descontor = total * 0.9
    print(f'Com desconto de 10%, o valor total é de R${descontor:.1f}')


