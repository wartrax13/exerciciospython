'''primeira = str(input())
segunda = str(input())

'''

primeira = 'AATTGGAA'
segunda = 'TG'
terceira =''
for letra in primeira:
    if letra in primeira and letra not in segunda:
        terceira += letra

print(terceira)