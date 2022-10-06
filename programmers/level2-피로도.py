def solution(k, dungeons):
    answer = [0]
    visited = []
    def rec(user, cnt, visited):
        if k <= 0:
            return
        answer[0] = max(answer[0], cnt)
        for i in range(len(dungeons)):
            if i not in visited and user >= dungeons[i][0]:
                visited.append(i)
                rec(user - dungeons[i][1], cnt + 1, visited)
                visited.pop()
    rec(k, 0, visited)
    return answer[0]