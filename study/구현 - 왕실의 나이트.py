k = input()
y = ord(k[0]) - ord('a')
x = int(k[-1]) - 1

result = 0

move = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]

for m in move:
    ny = y + m[0]
    nx = x + m[1]
    if (0 <= ny <= 7) and (0 <= nx <= 7):
        result += 1

print(result)