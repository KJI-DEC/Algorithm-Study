import sys

m = 1000000
primes = [True for _ in range(m)]

for i in range(2, int(m ** 0.6)):
    if primes[i]:
        for j in range(i * 2, m, i):
            primes[j] = False

while True:
    n = int(sys.stdin.readline())

    flag = False
    if n == 0:
        break
    for i in range(3, m):
        if primes[i]:
            if primes[n - i]:
                print("%d = %d + %d"%(n , i , n-i))
                flag = True
                break
    if not flag:
        print( "Goldbach's conjecture is wrong.")