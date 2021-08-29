import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
city = []

for _ in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))

chicken = [(i,j) for i in range(n) for j in range(n) if city[i][j] == 2]
home = [(a,b) for a in range(n) for b in range(n) if city[a][b] == 1]

minimum = sys.maxsize

for c in combinations(chicken, m):
    s = 0
    for h in home:
        s += min([abs(h[0] - i[0]) + abs(h[1] - i[1]) for i in c])
        if minimum <= s:
            break
    minimum = min(minimum, s)

print(minimum)