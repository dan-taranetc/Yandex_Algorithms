elem = int(input())
max = elem
max_count = 1

if elem == 0:
    print(elem)
else:
    while elem != 0:
        elem = int(input())
        if elem > max:
            max = elem
            max_count = 0
        if elem == max:
            max_count += 1
    print(max_count)
