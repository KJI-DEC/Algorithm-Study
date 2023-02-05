import sys
from heapq import heappush, heappop


n = int(sys.stdin.readline())
heap = []
cnt = 0
tmp_cnt = 0

for _ in range(n):
    tmp = int(sys.stdin.readline())
    heappush(heap, tmp)

for _ in range(n - 1):
    tmp_cnt = heappop(heap) + heappop(heap)
    heappush(heap, tmp_cnt)
    cnt += tmp_cnt

print(cnt)