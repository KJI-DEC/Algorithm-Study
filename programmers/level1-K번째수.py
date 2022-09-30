def solution(array, commands):
    answer = []
    for c in commands:
        tmp = sorted(array[c[0] - 1 : c[1]])
        answer.append(tmp[c[-1] - 1])
    return answer