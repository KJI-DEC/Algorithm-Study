def solution(s):
    answer = ""
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tmp = ""
    for i in s:
        if i.isdigit():
            answer += i
        else:
            tmp += i
            if tmp in numbers:
                answer += str(numbers.index(tmp))
                tmp = ""

    return int(answer)

# replace를 활용한다면 더 짧아질 것 같음!