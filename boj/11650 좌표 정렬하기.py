import sys

n = int(sys.stdin.readline())
x_y = []

for _ in range(n):
    x_y.append(list(map(int, sys.stdin.readline().split())))

x_y.sort()

for i in x_y:
    print(i[0], i[1])