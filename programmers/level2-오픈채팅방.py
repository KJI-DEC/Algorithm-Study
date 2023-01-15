def solution(record):
    answer = []
    users = {}

    for r in record:
        tmp = r.split()
        nickname = users.get(tmp[1], '')
        if len(tmp) == 3:
            nickname = tmp[-1]
        users[tmp[1]] = nickname

    for r in record:
        tmp = r.split()
        if tmp[0] == 'Enter':
            answer.append(f'{users[tmp[1]]}님이 들어왔습니다.')
        elif tmp[0] == 'Leave':
            answer.append(f'{users[tmp[1]]}님이 나갔습니다.')
    return answer