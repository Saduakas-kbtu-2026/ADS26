
import heapq

n = int(input())
a = list(map(int, input().split()))

a = [-x for x in a]
heapq.heapify(a)

while len(a) > 1:
    x = -heapq.heappop(a)
    y = -heapq.heappop(a)

    if x != y:
        heapq.heappush(a, -(x - y))

print(-a[0] if a else 0)
