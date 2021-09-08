N = int(input())
coords = []
for i in range(N):
    coords.append(list(map(int, input().split())))

summ = N*4
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        if (coords[i][0] == coords[j][0]  and abs(coords[i][1] - coords[j][1]) == 1) or (coords[i][1] == coords[j][1] and abs(coords[i][0] - coords[j][0]) == 1):
            summ -= 2

print(summ)

