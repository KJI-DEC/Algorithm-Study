import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    if n[::-1] == n:
        print("yes")
    else:
        print("no")