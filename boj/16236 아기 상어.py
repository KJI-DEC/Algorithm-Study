from collections import deque

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0


def find_fish(q_find, visited_find, shark_find, weight):
    fish = []
    while q_find:
        x, y = q_find.popleft()
        for v in range(4):
            nx = x + dx[v]
            ny = y + dy[v]
            if 0 <= nx < n and 0 <= ny < n:
                if visited_find[nx][ny] == 0 and data[nx][ny] <= weight:
                    q_find.append((nx, ny))
                    visited_find[nx][ny] = visited_find[x][y] + 1
                    if 0 < data[nx][ny] < weight:
                        fish.append([visited_find[nx][ny] - 1, nx, ny])
    fish.sort()
    if len(fish) == 0:
        return 0, 0
    data[shark_find[0]][shark_find[1]] = 0
    shark_find = [fish[0][1], fish[0][2], weight]
    data[fish[0][1]][fish[0][2]] = 9
    return fish[0][0], shark_find


visited = [[0 for _ in range(n)] for _ in range(n)]
shark = []
q = deque()
w = 2
cnt = 0

for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            q.append((i, j))
            visited[i][j] = 1
            shark = [i, j]
            break

while True:
    sec, n_shark = find_fish(q, visited, shark, w)
    if sec == 0:
        break
    result += sec
    shark = n_shark
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[n_shark[0]][n_shark[1]] = 1
    q = deque([(n_shark[0], n_shark[1])])
    cnt += 1
    if cnt == w:
        w += 1
        cnt = 0

print(result)