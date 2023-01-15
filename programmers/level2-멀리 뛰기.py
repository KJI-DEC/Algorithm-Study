def solution(n):
    answer = fib(n + 1)
    return answer % 1234567

def fib(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1
    for _ in range(1, n):
        a, b = b, b + a
    return a