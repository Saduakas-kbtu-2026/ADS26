
import heapq

n, k = map(int, input().split())
h = []
s = 0

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "insert":
        x = int(cmd[1])

        heapq.heappush(h, x)
        s += x

        if len(h) > k:
            s -= heapq.heappop(h)

    else:
        print(s)
