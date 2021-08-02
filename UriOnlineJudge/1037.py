n = float(input())

if n > 100.00 or n < 0:
    print('Fora de intervalo')
else:
    if n <= 25.00:
        print('Intervalo [0,25]')
    elif 25.00 < n <= 50.00:
        print('Intervalo (25,50]')
    elif 50.00 < n <= 75.00:
        print('Intervalo (50,75]')
    elif 75.00 < n <= 100.00:
        print('Intervalo (75,100]')
