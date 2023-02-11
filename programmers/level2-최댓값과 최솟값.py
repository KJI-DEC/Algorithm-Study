def solution(s):
    answer = ''
    numbers = list(map(int, s.split()))
    numbers.sort()
    answer = str(numbers[0]) + ' ' + str(numbers[-1])
    return answer