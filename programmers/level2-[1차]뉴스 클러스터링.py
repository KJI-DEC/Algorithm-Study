def solution(str1, str2):
    answer = 0
    cnt = 0

    br1 = breakStr(str1.lower())
    br2 = breakStr(str2.lower())

    for k in br1.keys():
        if br2.get(k) == None:
            continue
        else:
            cnt += min(br1[k], br2[k])

    if len(br1.keys()) == len(br2.keys()) == 0:
        return 65536

    answer = int(cnt / (sum(br2.values()) + sum(br1.values()) - cnt) * 65536)
    return answer


def breakStr(string):
    res = []
    dic = {}
    for i in range(len(string) - 1):
        if ord('a') <= ord(string[i]) <= ord('z') and ord('a') <= ord(string[i + 1]) <= ord('z'):
            res.append(string[i:i + 2])

    sres = set(res)

    for s in sres:
        dic[s] = res.count(s)
    print(dic)

    return dic