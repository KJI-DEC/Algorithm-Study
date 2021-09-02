import sys

n = int(sys.stdin.readline())

def prime(num):     #소수 찾기
    tmp = [1] * (num + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if tmp[i]:
            for j in range(i * 2, n + 1, i):
                tmp[j] = 0
    return [i for i in range(2, n + 1) if tmp[i]]

primes = prime(n)

if n == 1:  #1인 경우 0(소수 없으니까)
    print(0)
else:   #포인터로 소수 배열 가리키면서 연속 소수들의 합으로 n이 만들어지는지 확인
    ans = 0
    start, end = 0, 0
    tmp = primes[0]

    while start <= end:
        if tmp < n:
            end +=1
            if end < len(primes):
                tmp += primes[end]
            else:
                break
        else:
            if tmp == n:
                ans += 1
            tmp -= primes[start]
            start += 1
    print(ans)