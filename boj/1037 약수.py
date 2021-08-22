import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

a = min(l)
b = max(l)

print(a*b)