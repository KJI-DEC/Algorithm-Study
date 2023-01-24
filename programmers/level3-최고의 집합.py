def solution(n, s):
    answer = []
    if s // n == 0:
        return [-1]
    tmp = s // n
    r = s % n
    for _ in range(n - r):
        answer.append(tmp)
    for _ in range(r):
        answer.append(tmp + 1)
    return answer