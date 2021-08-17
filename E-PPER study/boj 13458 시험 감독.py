import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

cnt = n
for i in a:
    i -= b
    if i > 0:
        cnt += i // c
        if i % c != 0:
            cnt += 1

print(cnt)