def longway(seq):
    idx = -20
    left = [0]*len(seq)
    for i in range(len(seq)):
        if seq[i] == 2:
            idx = i
        if seq[i] == 1:
            left[i] = i - idx
    idx = 20
    ans = 0
    for i in range(len(seq)-1, -1, -1):
        if seq[i] == 2:
            idx = i
        if seq[i] == 1:
            momentans = min(idx - i, left[i])
            ans = max(ans, momentans)
    return ans


seq = list(map(int, input().split()))
print(longway(seq))