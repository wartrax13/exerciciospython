"""
Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez,
apenas os números ímpares.
"""

fim = int(input('Digite um número: '))
x = 1
while x <= fim:
    if x % 2 != 0:
        print(x)
    x+=1