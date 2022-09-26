#첫번째 rgb에 따라 가장 작은 비용을 구한 후, 최솟값 구하기
n = int(input().rstrip())
rgb = []
for i in range(n):
    tmp = list(map(int, input().rstrip().rsplit()))
    rgb.append(tmp)

paint = [[] for _ in range(n)]
paint[0] = rgb[0]

for i in range(1, n):
    paint[i] = [
        rgb[i][0] + min(paint[i - 1][1], paint[i - 1][2]),
        rgb[i][1] + min(paint[i - 1][0], paint[i - 1][2]),
        rgb[i][2] + min(paint[i - 1][0], paint[i - 1][1])
    ]

print(min(paint[n-1]))