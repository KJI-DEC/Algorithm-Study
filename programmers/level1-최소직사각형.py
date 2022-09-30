def solution(sizes):
    answer = 0
    x, y = max(max(i) for i in sizes), max(min(j) for j in sizes)
    answer = x * y
    return answer

#아래는 sum을 이용해 일차원 배열을 반환하고 그걸로 max 찾은 경우에 대한 다른 사람의 풀이
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)