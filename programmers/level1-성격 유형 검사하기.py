def solution(survey, choices):
    answer = ''
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i in range(len(survey)):
        if choices[i] > 4:
            dic[survey[i][1]] += choices[i] - 4
        elif choices[i] == 4:
            continue
        else:
            dic[survey[i][0]] += 4 - choices[i]

    key = list(dic.keys())

    for i in range(0, 8, 2):
        if dic[key[i]] >= dic[key[i + 1]]:
            answer += key[i]
        else:
            answer += key[i + 1]

    return answer