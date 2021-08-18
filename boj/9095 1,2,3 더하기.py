import sys

t = int(sys.stdin.readline())

def cnt(re):
    if re == 1:
        return 1
    elif re == 2:
        return 2
    elif re == 3:
        return 4
    else:
        return cnt(re - 1) + cnt(re - 2) + cnt(re -3)

for i in range(t):
    n = int(sys.stdin.readline())
    print(cnt(n))