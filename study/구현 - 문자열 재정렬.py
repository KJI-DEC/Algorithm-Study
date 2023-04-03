# s = list(input())
#
# s.sort()
# cnt = 0
# flag = 0
#
# for i in range(len(s)):
#     if s[i].isdigit():
#         cnt += int(s[i])
#     else:
#         flag = i
#         break
#
# s = s[i:]
# s.append(str(cnt))
# result = "".join(s)
# print(result)

data = input()
result = []
value = 0

for x in data:
    if x.isdigit():
        value += int(x)
    else:
        result.append(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))