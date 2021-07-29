notas = [0,0,0,0,0,0,0,0]
soma = 0
x = 0
while x < 7:
    notas[x] = float(input(f'Digite a {x+1} nota: '))
    soma += notas[x]
    x += 1
x=0
while x < 7:
    print(f'A nota {x} é: {notas[x]}')
    x += 1
print(f'Média = {soma / x:.2f}')