"""
Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada,
em vez de começar com 1 e 10.
"""
t = int(input('Qual tabuada? '))
x = int(input('Digite o início da tabuada: '))
fim = int(input('Digite o fim da tabuada: '))

while x <= fim:
    print(f'{t} x {x}')
    x += 1