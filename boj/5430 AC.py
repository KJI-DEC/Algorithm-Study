import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-2].split(',')
    flag = 0

    if n == 0:
        arr = deque()
    else:
        arr = deque(arr)

    dir = 0 #짝수=원래 방향, 홀수=반대방향
    for j in p:
        if j == "R":
            dir += 1
        elif j == "D":
            if len(arr) <= 0:
                flag = 1
                break
            else:
                if dir % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    if dir % 2 == 1:
        arr.reverse()
    if flag == 0:
        print("["+",".join(arr)+"]")
    else:
        print("error")