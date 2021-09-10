import sys

n, k = map(int, sys.stdin.readline().split())
t = [0] * 100001

def bfs():
    q = []
    q.append(n)
    while q:
        v = q.pop(0)
        if v == k:
            print(t[v])
            return
        for next in (v - 1, v + 1, v * 2):
            if 0 <= next < 100001 and not t[next]:
                t[next] = t[v] + 1
                q.append(next)

bfs()