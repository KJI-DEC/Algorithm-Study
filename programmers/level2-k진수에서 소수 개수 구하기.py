import math


def solution(n, k):
    answer = 0
    n_str = make(n, k)
    n_list = split_zero(n_str)
    for i in n_list:
        if i.isdigit():
            if int(i) == 1:
                continue
            elif is_prime(int(i)):
                answer += 1

    return answer


# k 진수 만들기
def make(n, k):
    # divmod() = (몫, 나머지)
    res = ""
    while n > 0:
        n, r = divmod(n, k)
        res += str(r)
    return res[::-1]


# 0으로 분리하기
def split_zero(n):
    return n.split('0')


# 소수 판별하기
def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True