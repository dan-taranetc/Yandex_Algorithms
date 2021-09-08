N = int(input())
seq = list(map(int, input().split()))

if 2*max(seq)-sum(seq)>0:
    print(2*max(seq)-sum(seq))
else:
    print(sum(seq))