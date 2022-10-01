def solution(numbers, target):
    answer = 0
    flag = (sum(numbers) - target) // 2

    def dfs(flag, i, cnt):
        for j in range(i, len(numbers)):
            tmp = flag
            tmp -= numbers[j]
            if tmp == 0:
                cnt += 1
            elif tmp > 0:
                cnt += dfs(tmp, j + 1, 0)
            else:
                continue
        return cnt

    return dfs(flag, 0, 0)