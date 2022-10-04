def solution(priorities, location):
    answer = 1
    mine = [0 for _ in range(len(priorities))]
    mine[location] = 1  # 내 문서 위치 저장

    while True:
        if len(priorities) == 0:
            return answer
        if priorities.index(max(priorities)) == 0:
            if mine[0] == 1:
                return answer
            else:
                priorities.pop(0)
                mine.pop(0)
                answer += 1
        else:
            tmp = priorities.pop(0)
            priorities.append(tmp)
            tmp = mine.pop(0)
            mine.append(tmp)
    return answer