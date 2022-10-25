def solution():
    n = int(input())
    h = list(map(int, input().rstrip().rsplit()))
    cnt = 0

    for i in range(2, n - 2):
        m = max(h[i - 2], h[i - 1], h[i + 1], h[i + 2])

        if h[i] > m:
            cnt += h[i] - m

    print(f"#{test_case} {cnt}")


T = 10

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    solution()