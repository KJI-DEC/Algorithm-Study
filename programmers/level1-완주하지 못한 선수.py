def solution(participant, completion):
    answer = ''
    dic = {}
    for p in participant:
        if (p not in dic):
            dic[p] = 1
        else:
            dic[p] += 1

    for c in completion:
        if (c in dic):
            dic[c] -= 1

    for k in dic:
        if (dic[k] > 0):
            return k

    return answer

#아래는 프로그래머스에 있던 풀이... collections도 알아간다...
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]