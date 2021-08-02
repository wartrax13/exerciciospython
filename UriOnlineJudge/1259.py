q = int(input())
par = []
imp = []
while q != 0:
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        imp.append(n)
    q -= 1
par.sort()
imp.sort(reverse=True)
for x in par:
    print(x)
for i in imp:
    print(i)