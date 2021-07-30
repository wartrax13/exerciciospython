i, im, f, fm = map(int, input().split())
m = 0
h = 0
if i > 24 or f > 24:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if i == f and im == fm:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    else:
        if f > i and fm >= im:
            h = f - i
            m = fm - im
        elif f > i and im > fm:
            h = (f - i) - 1
            m = 60 - (im - fm)
        elif i > f and fm >= im:
            h = 23 - (i - f)
            m = fm - im
        elif i > f and im > fm:
            h = 23 - (i - f)
            m = 60 - (im - fm)
        elif f == i and fm > im:
            m = fm - im
            h = f - i
        elif f == i and im > fm:
            h = 23
            m = 60 - (im - fm)

        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))

