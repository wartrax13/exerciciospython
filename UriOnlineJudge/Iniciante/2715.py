'''
Dividindo os Trabalhos I
entrada: 3
         2 3 5
saída: 0
       1
'''

'''while True:
    try:
        z = 2
        hash_table = []
        while z > 0:
            z -= 1
            n = int(input())
            lista = [int(x) for x in input().split(' ')]
            p = lista.pop(-1)
            soma = sum(lista)
            if soma <= p:
                print(p - soma)

            if soma > p:
                print(soma - p)
        print('')
        if z == 0:
            break
    except EOFError:
        break'''

while True:
    try:
        n = int(input())
        t = [int(x) for x in input().split()]
        i = 2
        dif = sum(t[i:]) - sum(t[:i])
        while(True):
            i += 1
            new = sum(t[i:]) - sum(t[:i])
            if new < 0:
                break
            dif = new
        print(dif)
    except EOFError:
        break