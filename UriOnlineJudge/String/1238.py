'''Combinador
2
Tpo oCder
aa bb
'''
c = 0
q = ''
n = int(input())
for i in range(n):
    a, b = input().split()
    ab = a + b
    v = (len(ab) + 1) // 2
    c = len(b) - len(a)
    if c == 0:
        for i in range(0, v):
            q = a[i] + b[i]
            print(q)
    else:
        x = ''
        for i in range(0, v-1):
            a = a[i] + b[i]
            b = a + b

        print(a[i])
