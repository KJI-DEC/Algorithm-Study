import sys

n = int(sys.stdin.readline())

def queen(c):
    for i in range(c):
        if row[c] == row[i] or abs(row[c] - row[i]) == c - i:
            return 0
    return 1

def dfs(depth):
    global ans
    if depth == n:
        ans += 1
    else:
        for i in range(n):
            row[depth] = i
            if queen(depth):
                dfs(depth + 1)

row = [0] * n
ans = 0
dfs(0)
print(ans)