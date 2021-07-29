"""
Faça um programa que leia uma expressão com parênteses.
Usando pilhas, verifique se os parenteses foram abertos e fechados na ordem correta.
Exemplo:
(()) ok
()()(()())
"""
expressao = input('Digite a sequencia de parenteses: ')
x = 0
pilha = []
while x < len(expressao):
    if expressao[x] == '(':
        pilha.append('(')
    if expressao[x] == ')':
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(')')  # Força a mensagem de erro.
            break
    x += 1
if len(pilha) == 0:
    print('Ok')
    print(topo)
else:
    print('Erro')
