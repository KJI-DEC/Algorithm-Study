n = int(input())

data = []
for i in range(0, n):
    data.append(int(input()))

data.sort()

for i in range(0, n):
    print(data[i])