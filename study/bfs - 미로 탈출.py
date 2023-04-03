from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque([(0, 0)])

while q:
    v = q.popleft()
    for i in range(4):
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 1:
                q.append((nx, ny))
                data[nx][ny] = data[v[0]][v[1]] + 1

print(data[n - 1][m - 1])