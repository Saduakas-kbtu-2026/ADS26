
import heapq

n, k = map(int, input().split())
a = list(map(int, input().split()))

heapq.heapify(a)
ops = 0

while a[0] < k:
    if len(a) < 2:
        print(-1)
        break

    x = heapq.heappop(a)
    y = heapq.heappop(a)

    heapq.heappush(a, x + 2 * y)
    ops += 1
else:
    print(ops)
