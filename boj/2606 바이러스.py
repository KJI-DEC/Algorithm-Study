import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
c = {}
visited = []

for i in range(n):
    c[i + 1] = set()

for j in range(m):
    a, b = map(int, sys.stdin.readline().split())
    c[a].add(b)
    c[b].add(a)

def dfs(idx, dic):
    for i in dic[idx]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)

dfs(1, c)
print(len(visited) - 1)