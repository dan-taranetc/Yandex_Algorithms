seq = list(map(int, input().split()))
mass = set()
ans = []
for i in seq:
    if i not in mass:
        mass.add(i)
        ans.append(i)
    else:
        if i in ans:
            ans.remove(i)
print(' '.join(str(i) for i in ans))