
sequencia = input("Digite a string: ")
def count_string(sequencia):
    contador = {}

    for letra in sequencia:
        contador[letra] = contador.get(letra, 0) + 1

    for chave, valor in contador.items():
        print(f"{chave}: {valor}x")

count_string(sequencia)