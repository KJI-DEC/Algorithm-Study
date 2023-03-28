n = int(input())
x_list = list(map(int, input().split()))

x_list.sort()
result = 0
mem = 0

for x in x_list:
    mem += 1
    if mem >= x: # 현재 길드에 포함된 사람이 현재의 공포도 이상이면 길드 결성
        result += 1
        mem = 0

print(result)