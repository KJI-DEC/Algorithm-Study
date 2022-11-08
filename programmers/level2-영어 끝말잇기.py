def solution(n, words):
    dic = {}
    _words = []

    for i in range(n):
        dic[i + 1] = []

    for i in range(len(words)):
        person = i % n + 1
        dic[person].append(words[i])

        if words[i] in _words:
            print(_words)
            return [person, len(dic[person])]

        _words.append(words[i])

        if i + 1 < len(words):
            if words[i][-1] != words[i + 1][0]:
                return [person % n + 1, len(dic[person % n + 1]) + 1]

    if len(words) == len(list(set(words))):
        return [0, 0]

    return [0, 0]