#Time Out

import sys
from itertools import combinations

while True:
    n = int(sys.stdin.readline())
    primes = []

    if n == 0:
        break

    for i in range(3, n + 1):
        flag = True
        if i > 1:
            for j in range(2, int(i ** 0.5 + 1)):
                if i % j == 0:
                    flag = False
                    break
        else:
            flag = False
        if (flag):
            primes.append(i)

    sumFlag = False
    for c in combinations(primes, 2):
        if c[0] + c[1] == n:
            print(n, "=", c[0], "+", c[1])
            sumFlag = False
            break
        else:
            sumFlag = True
    if sumFlag:
        print("Goldbach's conjecture is wrong.")