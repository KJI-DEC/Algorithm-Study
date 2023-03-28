n = int(input())
data = input().split()

# R U L D
dx = [0, -1, 0, 1]  # 세로
dy = [1, 0, -1, 0]  # 가로

move = {"R": 0, "U": 1, "L": 2, "D": 3}

nx, ny = 1, 1

for d in data:
    i = move[d]
    tx = nx + dx[i]
    ty = ny + dy[i]
    if (not 0 < tx <= n) or (not 0 < ty <= n):
        continue
    nx = tx
    ny = ty

print(nx, ny)