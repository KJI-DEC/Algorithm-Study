def solution(n, times):
    answer = 0
    l, r = 1, max(times) * n
    while l <= r:
        m = (l + r) // 2
        ppl = 0
        for t in times:
            ppl += m // t
            if ppl >= n:
                break
        if ppl >= n:
            answer = m
            r = m - 1
        else:
            l = m + 1
    return answer