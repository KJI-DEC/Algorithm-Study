def solution(genres, plays):
    answer = []
    gnr_sum = {}
    gnr_dict = {}
    for i in range(len(genres)):
        gen = gnr_dict.get(genres[i], [])
        gen.append((i, plays[i]))
        gnr_dict[genres[i]] = gen
        gen_sum = gnr_sum.get(genres[i], 0)
        gen_sum += plays[i]
        gnr_sum[genres[i]] = gen_sum

    sorted_sum = sorted(gnr_sum.items(), key=lambda item: item[1], reverse=True)

    for key in sorted_sum:
        tp_list = gnr_dict[key[0]]
        sorted_tp = sorted(tp_list, key=lambda x: x[1], reverse=True)
        for i in range(min(2, len(sorted_tp))):
            answer.append(sorted_tp[i][0])

    return answer
