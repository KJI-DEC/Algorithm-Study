import sys

min, max = map(int, sys.stdin.readline().split())
nums = [1 for _ in range(max - min + 1)]

n = 2
for n in range(2, max):
    if n ** 2 > max:
        break
    mult = min // (n ** 2)
    while mult * (n ** 2) <= max:
        if mult * (n ** 2) - min >= 0 and mult * (n ** 2) - min <= max - min:
            nums[mult * (n ** 2) - min] = 0
        mult += 1

print(sum(nums))