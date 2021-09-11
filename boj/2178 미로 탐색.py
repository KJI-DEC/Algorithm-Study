import sys

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = []
    q.append((0, 0))
    maze[0][0] = 1
    while q:
        node = q.pop(0)
        for i in range(4):
            x = node[0] + dx[i]
            y = node[1] + dy[i]
            if 0 <= x < n and 0 <= y < m and maze[x][y] == 1:
                q.append([x, y])
                maze[x][y] = maze[node[0]][node[1]] + 1
bfs()
print(maze[n - 1][m - 1])