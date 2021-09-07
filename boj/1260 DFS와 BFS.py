import sys

n, m, v = map(int, sys.stdin.readline().split())
l = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    l[x][y] = 1
    l[y][x] = 1

def dfs(v):
    print(v, end = ' ')
    visited[v] = 1
    for i in range(1, n + 1):
        if visited[i] == 0 and l[v][i] == 1:
            dfs(i)

def bfs(v):
    q = [v]
    visited[v] = 0
    while(q):
        v = q[0]
        print(v, end = ' ')
        q.pop(0)
        for i in range(1, n + 1):
            if visited[i] == 1 and l[v][i] == 1:
                q.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)