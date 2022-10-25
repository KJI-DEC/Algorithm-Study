import heapq


def solution():
    ans = 0
    d = int(input())
    h = list(map(int, input().rstrip().rsplit()))
    h.sort()
    for _ in range(d):
        h[-1] -= 1
        h[0] += 1
        h.sort()
        ans = h[-1] - h[0]
        if ans == 1:
            break

    print(f"#{test_case} {ans}")


T = 10

for test_case in range(1, T + 1):
    solution()
