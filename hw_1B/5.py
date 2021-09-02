from math import sqrt

d = int(input())
x, y = map(int, input().split())
lens = {}

if x >= 0 and y >= 0:
    if y <= d-x:
        print(0)
    else:
        if sqrt(x**2+y**2) == min(sqrt(x**2+y**2), sqrt((x-d)**2 + y**2), sqrt(x**2 + (y-d)**2)):
            print(1)
        elif sqrt((x-d)**2 + y**2) == min(sqrt(x**2+y**2), sqrt((x-d)**2 + y**2), sqrt(x**2 + (y-d)**2)):
            print(2)
        else:
            print(3)
else:
    if sqrt(x ** 2 + y ** 2) == min(sqrt(x ** 2 + y ** 2), sqrt((x - d) ** 2 + y ** 2), sqrt(x ** 2 + (y - d) ** 2)):
        print(1)
    elif sqrt((x - d) ** 2 + y ** 2) == min(sqrt(x ** 2 + y ** 2), sqrt((x - d) ** 2 + y ** 2),
                                            sqrt(x ** 2 + (y - d) ** 2)):
        print(2)
    else:
        print(3)