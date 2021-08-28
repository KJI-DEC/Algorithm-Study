#시간초과 뜸, dfs
import sys

def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if mem[i] and mem[j]:
                    start += s[i][j]
                elif not mem[i] and not mem[j]:
                    link += s[i][j]
        ans = min(ans, abs(start - link))

    for i in range(idx, n):
        if mem[i]:
            continue
        mem[i] = 1
        dfs(i + 1, cnt + 1)
        mem[i] = 0

n = int(sys.stdin.readline())
s = []
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))
mem = [0] * n
ans = sys.maxsize
dfs(0, 0)
print(ans)