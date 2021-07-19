'''
Data com mês por extenso.
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''
data = str(int)
def dataExtenso(data):
    meses = [(), ['janeiro', 31], ['fevereiro', 29], ['março', 31], ['abril', 30],
             ['maio', 31], ['junho', 30], ['julho', 31], ['agosto', 31], ['setembro', 30],
             ['outubro', 31], ['novembro', 30], ['dezembro', 31]]
    data = data.split('/')
    dia, mes, ano = int(data[0]), int(data[1]), int(data[2])
    if 0 < mes < 13 and 0 < dia <= meses[mes][1]:
        print(f'{dia} de {meses[mes][0]} de {ano}')
    else:
        print('NULL')


dataExtenso('1/12/2021')