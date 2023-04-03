n, m = map(int, input().split())

ice = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0


def rec(x, y):
    if (not 0 <= x < n) or (not 0 <= y < m):
        return False
    if ice[x][y] == '0':
        ice[x][y] = '1'
        for v in range(4):
            nx = x + dx[v]
            ny = y + dy[v]
            rec(nx, ny)
        return True
    return False


for i in range(n):
    for j in range(m):
        if rec(i, j):
            result += 1

print(result)
