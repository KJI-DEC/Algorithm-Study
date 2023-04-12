m, n, k = map(int, input().split())

squares = [list(map(int, input().split())) for _ in range(k)]
area = [[0 for _ in range(n)] for _ in range(m)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

result = 0
dim = []

# 사각형 그리기
for square in squares:
    x_start = min(square[0], square[2])
    x_end = max(square[0], square[2])
    y_start = min(square[1], square[3])
    y_end = max(square[1], square[3])
    for i in range(y_start, y_end):
        for j in range(x_start, x_end):
            area[i][j] = 1


# y_x 순서임
def dfs(x, y):
    if area[y][x] != 0:
        return 0
    area[y][x] = 1
    stack = [(x, y)]
    cnt = 0
    while stack:
        tx, ty = stack.pop()
        cnt += 1
        for v in range(4):
            nx = tx + dx[v]
            ny = ty + dy[v]
            if 0 <= nx < n and 0 <= ny < m:
                if area[ny][nx] == 0:
                    stack.append((nx, ny))
                    area[ny][nx] = 1
    return cnt


for i in range(m):
    for j in range(n):
        tmp = dfs(j, i)
        if tmp == 0:
            continue
        result += 1
        dim.append(tmp)


dim.sort()
print(result)
for d in dim:
    print(d, end=" ")