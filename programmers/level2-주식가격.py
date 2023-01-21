def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        tmp = 1
        for j in range(i + 1, len(prices) - 1):
            if prices[i] > prices[j]:
                break
            else:
                tmp += 1
        if len(answer) != i + 1:
            answer.append(tmp)
    answer.append(0)
    return answer

# stack에 담고 해당 값보다 큰 값이 있으면 뺌
# list를 반대로 append하고 .reverse() 사용?