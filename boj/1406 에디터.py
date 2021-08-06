import sys

editor = list(sys.stdin.readline().strip())
editor_r = []
m = int(sys.stdin.readline())

for _ in range (m):
    l = sys.stdin.readline().split()
    cmd = l[0]
    if cmd == "L":
        if editor:
            editor_r.append(editor.pop())
    elif cmd == "D":
        if editor_r:
            editor.append(editor_r.pop())
    elif cmd == "B":
        if editor:
            editor.pop()
    elif cmd == "P":
        editor.append(l[1])

print(''.join(editor + list(reversed(editor_r))))