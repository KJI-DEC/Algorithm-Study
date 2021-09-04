import sys
from math import sqrt

t = int(sys.stdin.readline())

m = 2000002
primes = [True for _ in range(m)]
primes[0] = False
primes[1] = False

for i in range(2, int(sqrt(m)) + 1):
    if primes[i]:
        for j in range(i * 2, m, i):
            primes[j] = False

arr = []
for i in range(2, m):
    if primes[i]:
        arr.append(i)

def prime(n):
    for i in range(0, len(arr)):
        if arr[i] * arr[i] > n:
            break
        if n % arr[i] == 0:
            return False
    return True

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    tie = a + b

    if tie < 4:
        print("NO")
    elif tie % 2 == 0:
        print("YES")
    else:
        tie -= 2
        if prime(tie):
            print("YES")
        else:
            print("NO")