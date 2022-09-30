def solution(nums):
    answer = 0
    tmp = list(set(nums))
    answer = min(len(nums)//2, len(tmp))
    return answer