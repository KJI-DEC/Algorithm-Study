import sys

n = int(sys.stdin.readline())

def check(num):
    for i in range(1, len(num) // 2 + 1):
        if num[-i:] == num[-i*2:-i]:
            return False
    return True

def sol(num):
    if len(num) == n:
        print(num)
        exit()
    for i in '123':
        if check(num + i):
            sol(num + i)

print(sol('1'))