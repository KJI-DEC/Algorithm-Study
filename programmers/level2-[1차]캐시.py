from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque([])

    if cacheSize == 0:
        return 5 * len(cities)

    for c in cities:
        city = c.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.appendleft(city)
        else:
            if len(cache) == cacheSize:
                cache.pop()
            cache.appendleft(city)
            answer += 5

    return answer