from math import sqrt, floor, ceil
x1, y1, x2, y2 = map(int, input().split())
x3, y3, r = map(int, input().split())
counter = 0

for i in range(max(y1, y3-r), min(y2, y3+r) + 1):
    a = min(x2, floor(x3 + sqrt(r**2 - (i-y3)**2)))
    b = max(x1, ceil(x3 - sqrt(r**2 - (i-y3)**2)))
    if a>=b:
        counter += a-b+1

print(counter)