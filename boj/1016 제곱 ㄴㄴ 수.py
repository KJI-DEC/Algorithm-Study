import sys
import math

min, max = map(int, sys.stdin.readline().split())

mult = []
n = int(math.sqrt(1000001000000)) + 1
for i in range(2, n):
    if i * i > 1000001000000:
        break
    mult.append(i * i)

cnt = 0
for num in range(min, max + 1):
    for m in mult:
        if num < m:
            break
        if num % m == 0:
            cnt += 1
            break

print(max - min + 1 - cnt)