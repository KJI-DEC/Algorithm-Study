
def solution(user_input):
    cnt = 0
    s = 0
    for i in range(len(user_input)):
        if user_input[i] == 'O':
            s += 1
            cnt += s
        else:
            s = 0
    total_score = cnt
    return total_score

if __name__=='__main__':
    user_input = input()
    if len(user_input) > 1000:
        print('입력 범위를 초과하였습니다.\n')
        exit(1)
    print(solution(user_input))