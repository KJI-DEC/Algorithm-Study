def solution(n):
    return fib(n) % 1234567


def fib(n):
    f = 1
    tmp = 1

    if n == 2:
        return 1

    for _ in range(1, n):
        f, tmp = tmp, tmp + f

    return f