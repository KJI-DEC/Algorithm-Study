def solution(s):
    answer = True
    o = []

    for a in s:
        if a == '(':
            o.append(a)
        else:
            if len(o) < 1:
                return False
            else:
                o.pop()
    if len(o) > 0:
        return False
    return True