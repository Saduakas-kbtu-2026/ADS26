
import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))

a = [-x for x in a]
heapq.heapify(a)

ans = 0

for _ in range(m):
    k = -heapq.heappop(a)
    ans += k

    if k > 1:
        heapq.heappush(a, -(k - 1))

print(ans)
