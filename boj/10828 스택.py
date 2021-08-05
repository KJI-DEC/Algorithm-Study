import sys

n = int(sys.stdin.readline())
s = []

for _ in range(n):
    l = sys.stdin.readline().split()
    if l[0] == "push":
        s.append(l[1])
    elif l[0] == "pop":
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif l[0] == "size":
        print(len(s))
    elif l[0] == "empty":
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif l[0] == "top":
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])