def solution(msg):
    answer = []
    dic = {}
    for i in range(ord('A'), ord('Z') + 1):
        dic[chr(i)] = i - ord('A') + 1

    i = 0
    while True:
        flag = 1
        j = len(msg)
        while j > 0:
            if msg[i:j] in dic:
                answer.append(dic[msg[i:j]])
                dic[msg[i:j + 1]] = len(dic.values()) + 1
                flag = len(msg[i:j])
                break
            j -= 1
        i += flag
        if i > len(msg):
            break
    return answer