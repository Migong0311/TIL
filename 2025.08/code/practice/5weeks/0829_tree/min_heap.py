import heapq

heap = []

lst = [6, 5, 4, 1, 3, 2, 9, 8, 7, 10]

for i in range(10):
    heapq.heappush(heap, lst[i])

print(heap)

for i in range(10):
    print(heapq.heappop(heap),end=',')

