import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    l = list(map(int, sys.stdin.readline().split()))
    target = l[m]
    target_i = list(0 for i in range(len(l)))
    target_i[m] = 1
    cnt = 0

    while(True):
        if l[0] == max(l):
            cnt += 1
            if target_i[0] == 1:
                print(cnt)
                break
            else:
                l.pop(0)
                target_i.pop(0)
        else:
            l.append(l.pop(0))
            target_i.append(target_i.pop(0))