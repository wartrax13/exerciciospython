valor = []
def nesima(n):
    for i in range(1,10): #para 9 elementos
        if i < 10:
            valor.append(n+i)
            print(valor)
nesima(0)