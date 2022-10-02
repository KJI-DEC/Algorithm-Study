import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    tmp = scoville[0]
    if tmp >= K:
        return answer
    while len(scoville) > 1:
        tmp = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        answer += 1
        heapq.heappush(scoville, tmp)
        tmp = scoville[0]
        if tmp >= K:
            return answer

    if heapq.heappop(scoville) < K:
        return -1

    return answer