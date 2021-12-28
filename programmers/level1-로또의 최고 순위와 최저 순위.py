# def solution(lottos, win_nums):
#     answer = []
#     cnt = 0
#     for n in win_nums:
#         if n in lottos:
#             cnt += 1
#
#     if cnt == 6:
#         answer.append(1)
#     elif cnt == 5:
#         answer.append(2)
#     elif cnt == 4:
#         answer.append(3)
#     elif cnt == 3:
#         answer.append(4)
#     elif cnt == 2:
#         answer.append(5)
#     elif cnt == 1 or cnt == 0:
#         answer.append(6)
#
#     cnt += lottos.count(0)
#
#     if cnt == 6:
#         answer.append(1)
#     elif cnt == 5:
#         answer.append(2)
#     elif cnt == 4:
#         answer.append(3)
#     elif cnt == 3:
#         answer.append(4)
#     elif cnt == 2:
#         answer.append(5)
#     elif cnt == 1 or cnt == 0:
#         answer.append(6)
#
#     answer.sort()
#
#     return answer

def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1

    answer.append(rank[cnt_0 + ans])
    answer.append(rank[ans])

    return answer