#Calculo fatorial
def fatorial(n):
    fat = 1
    while n>1:
        fat*=n
        n-=1
    return fat
print(fatorial(4))
