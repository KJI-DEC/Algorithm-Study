import sys

n = int(sys.stdin.readline())
o = []
flag = []

for _ in range(n):
    ps = list(sys.stdin.readline())
    sum = 0
    for i in ps:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")