import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

for i in l:
    if i > 1:
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                n -= 1
                break
    elif i == 1:
        n -= 1

print(n)