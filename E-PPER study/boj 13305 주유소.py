import sys

n = int(sys.stdin.readline())
o = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))

result = o[0] * l[0]
cost = l[0]
distance = 0

for i in range(1, n - 1):
    if l[i] < cost:
        result += cost * distance
        distance = o[i]
        cost = l[i]
    else:
        distance += o[i]

    if i == n - 2:
        result += cost * distance

print(result)