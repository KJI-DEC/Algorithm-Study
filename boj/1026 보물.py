import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
ans = 0

for _ in range(n):
    ans += a.pop(a.index(min(a))) * b.pop(b.index(max(b)))

print(ans)

