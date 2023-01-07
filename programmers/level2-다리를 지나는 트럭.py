from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = bridge_length + 1
    on_b = deque()
    tw = deque(truck_weights)

    for _ in range(bridge_length - 1):
        on_b.append(0)

    on_bw = tw.popleft()
    on_b.append(on_bw)

    while True:
        if len(tw) == 0:
            return answer
        answer += 1
        on_bw -= on_b.popleft()
        t = tw.popleft()

        if on_bw + t > weight:
            tw.appendleft(t)
            on_b.append(0)
        else:
            on_b.append(t)
            on_bw += t

    return answer