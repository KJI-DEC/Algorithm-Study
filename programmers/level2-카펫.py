def solution(brown, yellow):
    answer = []
    carpet = brown + yellow
    if int(carpet ** (1 / 2)) == carpet ** (1 / 2):  # 중근일 경우
        return [carpet ** (1 / 2), carpet ** (1 / 2)]
    for x in range(carpet // 3, 2, -1):  # 아닌 경우
        if x ** 2 - (brown // 2 + 2) * x + carpet == 0:
            answer.append(x)
        if len(answer) == 2:
            return answer

    return answer