import sys
from heapq import heappush, heappop, heappushpop

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    for data in list(map(int,sys.stdin.readline().split())):
        if len(heap)<N:
            heappush(heap, data)
        top = heap[0]
        if top<data:
            heappushpop(heap, data) # data를 push하고 가장 작은 원소 반환

print(heappop(heap)) # 가장 작은 원소 반환
