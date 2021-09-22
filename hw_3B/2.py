seq = list(map(int, input().split()))
mass = set()
for i in seq:
    if i in mass:
        print('YES')
    else:
        mass.add(i)
        print('NO')