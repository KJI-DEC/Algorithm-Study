import sys

n = int(sys.stdin.readline())
s = []
a = 1
flag = 0
ans = []

for _ in range(n):
    k = int(sys.stdin.readline())
    while(a <= k):
        s.append(a)
        a += 1
        ans.append("+")
    if s[-1] == k:
        s.pop()
        ans.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    print("\n".join(ans))