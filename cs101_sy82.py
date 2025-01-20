from collections import deque
n = int(input())
def min_way(n):
    min_time = 100002
    q = deque([(1, 0)])
    visited = set([1])
    while q:
        x, time = q.popleft()
        if x == n:
            min_time = min(min_time, time)
        if x > n:
            continue
        for i in [0, 1]:
            if i == 0 and x + 1 not in visited and x + 1 <= n:
                visited.add(x + 1)
                q.append((x + 1, time + 1))
            if i == 1 and 2 * x not in visited and 2 * x <= n:
                visited.add(2 * x)
                q.append((x * 2, time + 1))
    return min_time
a = min_way(n)
print(a)