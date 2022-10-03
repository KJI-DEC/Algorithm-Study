# def solution(name):
#     ln = len(name)
#     answer = 0
#     tmp = [-1, -1, -1]  # a 시작 지점, a 끝나는 지점, a 개수
#     dic = {}
#     move = [ln - 1]
#     while name[move[0]] == 'A' and move[0] > 0:
#         move[0] -= 1

#     for i in range(ln):
#         n = abs(ord(name[i]) - ord('A'))
#         answer += min(n, 26 - n)  # 문자 바꿀 때 드는 횟수
#         if n == 0:
#             if tmp[0] == -1:  # 새롭게 a가 시작하는 경우
#                 tmp = [i, i, 1]
#             else:  # 기존에 a가 있었던 경우
#                 tmp[1] += 1
#                 tmp[2] += 1
#         else:
#             if tmp[0] != -1:  # a가 아닌데 반복된 a가 이전에 존재했던 경우
#                 dic[(tmp[0], tmp[1])] = tmp[2]
#                 tmp = [-1, -1, -1]

#     if tmp[0] != -1:
#         dic[(tmp[0], tmp[1])] = tmp[2]

#     for (start, end), cnt in dic.items():
#         if(start == 0):
#             move.append(ln - end - 1)
#         elif(end == ln - 1):
#             move.append(ln - end + start - 2)
#         else:
#             left = (ln - end - 1) * 2 + start
#             right = (start - 1) * 2 + ln - end - 1
#             if left >= 0:
#                 move.append(left)
#             if right >= 0:
#                 move.append(right)

#     answer += min(move)
#     return answer

def solution(name):
    answer = 0
    min_move = len(name) - 1

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)  # 문자 변경 시 움직이는 횟수
        next = i + 1

        while next < len(name) and name[next] == 'A':  # 반복되는 A 찾기
            next += 1

        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])  # 좌측 선이동, 우측 선이동 중 최솟값 구하기

    answer += min_move
    return answer

print(solution("BBA"))