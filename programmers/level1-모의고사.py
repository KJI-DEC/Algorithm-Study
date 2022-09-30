def solution(answers):
    answer = []
    cnt = [0,0,0]
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if(answers[i] == a[i%len(a)]):
            cnt[0] += 1
        if(answers[i] == b[i%len(b)]):
            cnt[1] += 1
        if(answers[i] == c[i%len(c)]):
            cnt[2] += 1
    if(max(cnt) == cnt[0]):
        answer.append(1)
    if(max(cnt) == cnt[1]):
        answer.append(2)
    if(max(cnt) == cnt[2]):
        answer.append(3)
    return answer

#아래는 enumerate를 이용해 마지막 if문을 반복문으로 돌린 방안
def solution(answers):
    answer = []
    cnt = [0,0,0]
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if(answers[i] == a[i%len(a)]):
            cnt[0] += 1
        if(answers[i] == b[i%len(b)]):
            cnt[1] += 1
        if(answers[i] == c[i%len(c)]):
            cnt[2] += 1

    for i, c in enumerate(cnt):
        if c == max(cnt):
            answer.append(i + 1)
    return answer