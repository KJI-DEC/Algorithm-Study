import sys

n = int(sys.stdin.readline())

data = [0 for _ in range(0,10001)]

for i in range(0, n):
    num = int(sys.stdin.readline())
    data[num - 1] += 1

for i in range(len(data)):
    for j in range(0, data[i]):
        print(i + 1)