def solution(progresses, speeds):
    answer = []
    days = []
    n = len(progresses)

    for i in range(n):
        if (100 - progresses[i]) % speeds[i] > 0:
            days.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            days.append((100 - progresses[i]) // speeds[i])

    tmp = days[0]
    cnt = 0
    for i in range(n):
        days[i] -= tmp
        if days[i] > 0:
            answer.append(cnt)
            cnt = 1
            tmp += days[i]
        else:
            cnt += 1
    answer.append(n - sum(answer))
    return answer