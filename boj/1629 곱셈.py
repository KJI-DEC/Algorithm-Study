def solution(x, y, z):
    if y == 1:
        return x % z
    else:
        t = solution(x, y // 2, z)
        if y % 2 == 0:
            return t ** 2 % z
        else:
            return t ** 2 * x % z


a, b, c = map(int, input().split())

print(solution(a, b, c))