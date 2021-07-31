#TUPLAS USADAS COMO REGISTRO - PAGINA 52

lax_cordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
#Desempacotamento(unpacking)
for country, _ in traveler_ids:
    print(country)
# -----
latitude, longitude = lax_cordinates # desempacotamento de tupla
print(longitude)
