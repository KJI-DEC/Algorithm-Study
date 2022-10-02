def solution(phone_book):
    answer = True
    tmp = []

    for p in phone_book:
        tmp.append((p, len(p)))

    tmp.sort()

    for i in range(len(tmp) - 1):
        if tmp[i][0] == tmp[i + 1][0][:len(tmp[i][0])]:
            return False

    return answer