import heapq

def solution(operations):
    answer = []
    hq = []
    heapq.heapify(hq)
    for o in operations:
        if o[0] == "I":
            heapq.heappush(hq, int(o[2:]))
        elif len(hq) == 0:
            continue
        elif o[0] == "D":
            if o[2] == "-":
                heapq.heappop(hq)
            else:
                hq.remove(max(hq))
                heapq.heapify(hq)

    if len(hq) == 0:
        return [0, 0]
    else:
        return [max(hq), min(hq)]
    return answer