s = input()

dic = {}
result = ""
odd = ""

for c in s:
    if dic.get(c, 0) == 0:
        dic[c] = 1
    else:
        dic[c] += 1

sorted_key = sorted(dic.keys())

for key in sorted_key:
    if dic[key] % 2 == 0:
        continue
    if odd != "":
        result = "I'm Sorry Hansoo"
        break
    odd += key

if len(result) == 0:
    for key in sorted_key:
        cnt = dic[key] // 2
        result += key * cnt
    if len(odd) == 1:
        result += odd + result[::-1]
    else:
        result += result[::-1]

print(result)