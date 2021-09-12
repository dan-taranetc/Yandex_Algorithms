def dirs(seq):
    max_el = seq[0]
    for i in range(len(seq)):
        if seq[i] > max_el:
            max_el = seq[i]
    return sum(seq)-max_el


n = int(input())
seq = list(map(int, input().split()))
print(dirs(seq))