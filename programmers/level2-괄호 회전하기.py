def solution(s):
    answer = 0
    for _ in range(len(s)):
        if isbr(s):
            answer += 1
        s = movebr(s)
    return answer

def movebr(s):
    s = s[1:] + s[0]
    return s

def isbr(s):
    st = []
    for i in s:
        if i == '{' or i == '[' or i == '(':
            st.append(i)
        elif len(st) != 0:
            tmp = st.pop()
            if tmp == '{' and i != '}':
                return False
            elif tmp == '[' and i != ']':
                return False
            elif tmp == '(' and i != ')':
                return False
        else:
            return False
    if len(st) == 0:
        return True
    return False