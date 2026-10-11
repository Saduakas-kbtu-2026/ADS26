
import heapq

n = int(input())
a = list(map(int, input().split()))

heapq.heapify(a)
cost = 0

while len(a) > 1:
    s = heapq.heappop(a) + heapq.heappop(a)
    cost += s
    heapq.heappush(a, s)

print(cost)
