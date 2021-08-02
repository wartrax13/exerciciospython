#A corrida de lesmas




while True:
    try:
        n1 = int(input())
        lesmas1 = list(int(x) for x in input().split(' '))
        l1_max = max(lesmas1)
        n2 = int(input())
        lesmas2 = list(int(x) for x in input().split(' '))
        l2_max = max(lesmas2)
        n3 = int(input())
        lesmas3 = list(int(x) for x in input().split(' '))
        l3_max = max(lesmas3)

        if l1_max >= 20:
            print('3')
        elif 20 > l1_max >= 10:
            print('2')
        elif l1_max < 10:
            print('1')

        if l2_max >= 20:
            print('3')
        elif 20 > l2_max >= 10:
            print('2')
        elif l2_max < 10:
            print('1')

        if l3_max >= 20:
            print('3')
        elif 20 > l3_max >= 10:
            print('2')
        elif l3_max < 10:
            print('1')
    except EOFError:
        break