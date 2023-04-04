n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y = n // 2, n // 2

result = 0

for i in range(2 * n - 1):  # 방향 전환 횟수
    for j in range(i // 2 + 1):
        idx = i % 4
        tx = dx[idx]
        ty = dy[idx]
        x += tx
        y += ty
        if not 0 <= x < n or not 0 <= y < n:
            break
        sand = data[x][y]
        data[x][y] = 0
        sand_dict = {
            1: int(sand * 0.01),
            2: int(sand * 0.02),
            5: int(sand * 0.05),
            7: int(sand * 0.07),
            10: int(sand * 0.1),
        }
        sand_dict[0] = sand - (sand_dict[1] * 2 + sand_dict[2] * 2 + sand_dict[5] + sand_dict[7] * 2 + sand_dict[10] * 2)

        torn_dict = {
            5: [(x + tx * 2, y + ty * 2)],
            7: [(x + ty, y + tx), (x - ty, y - tx)],
            2: [(x + 2 * ty, y + 2 * tx), (x - 2 * ty, y - 2 * tx)],
            0: [(x + tx, y + ty)]
        }

        if idx % 2 == 0:
            torn_dict[10] = [(x + ty, y + ty), (x - ty, y + ty)]
            torn_dict[1] = [(x + ty, y - ty), (x - ty, y - ty)]
        else:
            torn_dict[10] = [(x + tx, y + tx), (x + tx, y - tx)]
            torn_dict[1] = [(x - tx, y + tx), (x - tx, y - tx)]

        for per, position in torn_dict.items():
            for p in position:
                if 0 <= p[0] < n and 0 <= p[1] < n:
                    data[p[0]][p[1]] += sand_dict[per]
                else:
                    result += sand_dict[per]

print(result)