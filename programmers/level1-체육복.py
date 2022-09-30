def solution(n, lost, reserve):
    _reserve = list(set(reserve) - set(lost))
    _lost = list(set(lost) - set(reserve))
    answer = n - len(_lost)
    for r in _reserve:
        if(r - 1 in _lost or r + 1 in _lost):
            answer += 1
    answer = min(n, answer)
    return answer