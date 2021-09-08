import sys

n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
apt = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if m[x][y] == 1:
        cnt += 1
        m[x][y] = 0
        for i in range(4):
            xp = x + dx[i]
            yp = y + dy[i]
            dfs(xp, yp)
        return True
    return False

cnt = 0
ans = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            apt.append(cnt)
            ans += 1
            cnt = 0

apt.sort()
print(ans)
for a in apt:
    print(a)