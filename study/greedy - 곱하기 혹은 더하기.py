s = input()
result = 0

for n in s:
    n = int(n)
    if n <= 1 or result <= 1:
        result += n
    else:
        result *= n

print(result)