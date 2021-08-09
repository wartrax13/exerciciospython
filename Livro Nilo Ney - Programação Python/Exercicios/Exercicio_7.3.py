primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = ""
# Para cada letra na primeira string
for letra in primeira:
    # Se a letra está na segunda string (comum a ambas)
    # Para evitar repetidas, não deve estar na terceira.
    if letra in primeira and letra not in segunda:
        terceira += letra

for letra in segunda:
    if letra in segunda and letra not in primeira:
        terceira += letra

if terceira == "":
    print("Caracteres comuns não encontrados.")
else:
    print(f"Caracteres em comum: {terceira}")