import sys

n = int(sys.stdin.readline())
d = []

for _ in range(n):
    l = sys.stdin.readline().split()
    if l[0] == "push_front":
        d.insert(0, l[1])
    elif l[0] == "push_back":
        d.append(l[1])
    elif l[0] == "pop_front":
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop(0))
    elif l[0] == "pop_back":
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif l[0] == "size":
        print(len(d))
    elif l[0] == "empty":
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif l[0] == "front":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif l[0] == "back":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])