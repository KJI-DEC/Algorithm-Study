n, k = map(int, input().split())
cnt = 0

# my code
while n > 1:
    if n <= 1:
        break
    if n % k == 0:
        n /= k
    else:
        n -= 1
    cnt += 1

print(cnt)

# lecturer's code
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    n //= k

result += (n - 1)
print(result)