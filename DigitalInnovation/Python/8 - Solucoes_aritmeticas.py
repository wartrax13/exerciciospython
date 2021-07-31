

n = int(input())
while n >= 1:
    n -= 1
    placa = input().split('-')
    if len(placa[0]) != 3:
        print('FALHA')
    elif placa[0] != placa[0].upper():
        print('FALHA')
    elif placa[0].isalpha() == False:
        print('FALHA')
    elif not placa[1].isdigit():
        print('FALHA')

    else:
        if placa[1][3:] == '4' or placa[1][3:] == '3':
            print('TERCA')
        elif placa[1][3:] == '1' or placa[1][3:] == '2':
            print('SEGUNDA')
        elif placa[1][3:] == '5' or placa[1][3:] == '6':
            print('QUARTA')
        elif placa[1][3:] == '7' or placa[1][3:] == '8':
            print('QUINTA')
        elif placa[1][3:] == '9' or placa[1][3:] == '0':
            print('SEXTA')
        else:
            print('FALHA')
