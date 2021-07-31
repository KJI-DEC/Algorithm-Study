#Binary Search
n = int(input())
a = list(map(int, input().split()))
m = int(input())
m_l = list(map(int, input().split()))

a.sort()    #binary search 전에 sort해야 함

for i in m_l:
    search = i  #찾으려는 수

    left = 0
    right = n - 1
    ans = 0

    while(left <= right):
        mid = (left + right) // 2
        if a[mid] == search:
            ans = 1
            break
        elif search < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print(ans)