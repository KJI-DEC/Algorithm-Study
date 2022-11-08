def solution(s):
    answer = []
    tmp = ""
    dic = {}
    for i in s:
        if i.isdigit():
            tmp += i
        elif i in [" ", ",", "{", "}"] and tmp != "":
            if dic.get(int(tmp)) != None:
                dic[int(tmp)] += 1
                tmp = ""
            else:
                dic[int(tmp)] = 0
                tmp = ""
    _dic = sorted(dic.items(), key = lambda item: item[1], reverse = True)
    return [i[0] for i in _dic]