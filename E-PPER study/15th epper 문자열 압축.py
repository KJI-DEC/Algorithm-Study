def solution(user_input):
    result = ""
    cnt = 0
    if user_input[0] == '1':
        result += '1'
    for i in range(len(user_input) - 1):
        if user_input[i] != user_input[i + 1]:
            result += chr(ord('A') + cnt)
            cnt = 0
        else:
            cnt += 1
    result += chr(ord('A') + cnt)
    return result


user_input = input()
print(solution(user_input))