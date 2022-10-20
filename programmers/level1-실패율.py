def solution(N, stages):
    answer = []
    fail = []
    ppl = len(stages)
    for i in range(1, N + 1):
        cnt = stages.count(i)
        fail.append([i,cnt/ppl])
        ppl -= cnt
        if ppl == 0:
            ppl = 1
    answer = list(zip(*sorted(fail, key = lambda x: x[1], reverse = True)))[0]
    return answer