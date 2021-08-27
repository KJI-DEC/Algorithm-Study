import sys

n, m = map(int, sys.stdin.readline().split())

N, M = n, m

while M != 0:
    tmp = N % M
    N = M
    M = tmp
print(N)

mul = (n * m) / N
print(int(mul))