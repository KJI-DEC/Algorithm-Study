import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

card.sort()

dic = {}

for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for j in range(m):
    if l[j] in dic:
        print(dic[l[j]], end=" ")
    else:
        print(0, end = " ")