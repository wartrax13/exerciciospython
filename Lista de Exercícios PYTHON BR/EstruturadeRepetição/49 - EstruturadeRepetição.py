'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.

'''
def troca(vet):
    for i in range(3):
        if vet[i] >= 0:
            vet[i] = 1
        else:
            vet[i] = 0
    return vet

vet = [0]*3
for i in range(3):
    vet[i] = input('Digite um valor: ')
print(vet)
troca(vet)
print(vet)