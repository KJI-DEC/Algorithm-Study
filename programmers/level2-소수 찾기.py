import math
import itertools


def solution(numbers):
    answer = 0
    integers = []
    combs = []

    for n in numbers:
        integers.append(ord(n) - ord("0"))

    for i in range(len(integers)):
        i_comb = itertools.permutations(integers, i + 1)
        for n in list(i_comb):
            tmp = 0
            for j in range(i + 1):
                tmp += 10 ** (i - j) * n[j]
            combs.append(tmp)

    def isPrime(i):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                return False
        return True

    combs = set(combs)

    for c in combs:
        if c == 0 or c == 1:
            continue
        if isPrime(c):
            answer += 1

    return answer