import sys

n = int(sys.stdin.readline())
words = []

for _ in range(n):
    words.append(sys.stdin.readline().strip())

words = list(set(words))
words.sort()
words.sort(key=len)

for word in words:
    print(word)


