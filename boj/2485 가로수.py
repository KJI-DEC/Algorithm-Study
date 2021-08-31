import sys

n = int(sys.stdin.readline())

trees = [int(sys.stdin.readline()) for _ in range(n)]
distances = [abs(trees[i + 1] - trees[i]) for i in range(n - 1)]

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

tmp = distances[0]
for d in distances:
    tmp = gcd(tmp, d)

num_tree = (max(trees) - min(trees)) // tmp + 1
print(num_tree - n)