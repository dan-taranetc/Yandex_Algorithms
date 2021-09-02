N, i, j = map(int, input().split())
if i < j:
    print(min(j-i-1, N-j+i-1))
else:
    print(min(i-j-1, N - i + j - 1))