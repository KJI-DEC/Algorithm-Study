def solution(n):
    answer = fib(n)
    return answer

def fib(n):
    if n <= 2:
        return n
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007

# n = 1인 경우, 1 -> 1
# n = 2인 경우, 2 -> 11, =
# n = 3인 경우, 3 -> 111, 1=, =1
# n = 4인 경우, 5 -> 1111, 11=, 1=1, =11, ==
# n = 5인 경우, 8
# n = 6인 경우, 13
# fib!