def solution(id_list, report, k):
    answer = []
    id_report = {}
    report_id = {}
    stop = {}

    for i in id_list:
        id_report[i] = []
        report_id[i] = []
        stop[i] = False

    for r in report:
        a, b = map(str, r.rsplit())  # 내 id, 신고한 id
        if a in report_id[b]:
            continue
        id_report[a].append(b)
        report_id[b].append(a)

    for i in id_list:
        if len(report_id[i]) >= k:
            stop[i] = True

    for i in id_list:
        tmp = 0
        for k in id_report[i]:
            if stop[k]:
                tmp += 1
        answer.append(tmp)

    return answer

# 다른 사람 풀이... 이렇게 했어야...
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     reports = {x : 0 for x in id_list}
#
#     for r in set(report):
#         reports[r.split()[1]] += 1
#
#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1
#
#     return answer