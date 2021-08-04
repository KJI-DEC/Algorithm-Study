import sys

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

data.sort()

for d in num:
    search = d

    left = 0
    right = n - 1
    ans = 0

    while(left <= right):
        mid = (left + right) // 2
        if data[mid] == search:
            ans = 1
            break
        elif search < data[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print(ans, end=" ")