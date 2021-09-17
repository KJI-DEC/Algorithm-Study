import sys

def solution(n, r, c):
    result = 0
    while n > 0:
        x = 2 ** (n - 1)
        if n > 1:
            if x > r and x <= c:
                result += x ** 2
                c -= x
            elif x <= r and x > c:
                result += (x ** 2) * 2
                r -= x
            elif x <= r and x <= c:
                result += (x ** 2) * 3
                r -= x
                c -= x
        elif n == 1:
            if r == 0 and c == 1:
                result += 1
            elif r == 1 and c == 0:
                result += 2
            elif r == 1 and c == 1:
                result += 3
        n -= 1
    return result

n, r, c = map(int, sys.stdin.readline().split())
ans = solution(n, r, c)
print(ans)