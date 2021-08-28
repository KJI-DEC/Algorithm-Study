import sys
from itertools import combinations

def sol():
    global ans
    for i in combinations(mem, n//2):
        start = list(i)
        link = list(set(mem) - set(start))

        starts = list(combinations(start, 2))
        links = list(combinations(link, 2))

        start_sum = 0
        for x, y in starts:
            start_sum += (s[x][y] + s[y][x])

        link_sum = 0
        for x, y in links:
            link_sum += (s[x][y] + s[y][x])

        ans = min(ans, abs(start_sum - link_sum))

n = int(sys.stdin.readline())
s = []
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))
mem = [i for i in range(n)]
ans = sys.maxsize
sol()
print(ans)
