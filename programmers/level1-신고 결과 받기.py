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