import sys

n, k = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, n + 1)]
ans = []
num = 0

for i in range(n):
    num += k - 1
    if num >= len(arr):
        num %= len(arr)
    ans.append(arr.pop(num))

print("<", end="")
print(", ".join(map(str, ans)), end="")
print(">", end="")