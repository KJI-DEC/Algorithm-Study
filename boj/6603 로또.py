import sys

def dfs(idx, d):
    if d == 6:
        print(" ".join(map(str, l)))
        return

    for i in range(idx, k):
        l[d] = s[i]
        dfs(i+1, d+1)

while True:
    s = list(map(int, sys.stdin.readline().split()))
    k = s.pop(0)

    if k == 0:
        break

    l = [0] * 6
    dfs(0, 0)
    print()