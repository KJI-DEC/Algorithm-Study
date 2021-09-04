import sys

def m(a, d, n):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d < n - 1:
        x = pow(x, 2, n)
        d <<= 1
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def p(n):
    if 1 < n < 4:
        return True
    if n < 2 or n & 1 < 1:
        return False
    d = n - 1
    while d % 2 - 1:
        d >>= 1
    return all(m(a, d, n) for a in (2, 3, 5, 7, 11, 13, 17) if a < n)

for _ in[0]*int(input()):
    a = sum(map(int, sys.stdin.readline().split()))
    print('YES' if a > 3 and (a % 2 == 0 or p(a - 2)) else 'NO')