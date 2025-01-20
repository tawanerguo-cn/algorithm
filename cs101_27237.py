from collections import deque
start_and_end = []
while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    start_and_end.append((n, m))
def min_step(n, m):
    visited = set()
    visited.add((n))
    q = deque()
    q.append((n, 0, []))
    while q:
        x, step, way = q.popleft()
        if x == m:
            return step, way
        if 3 * x not in visited and step <= 24:
            way_H = way + ['H']
            q.append((3 * x, step + 1, way_H))
            visited.add(3 * x)
        if x // 2 not in visited and step <= 24:
            way_O = way + ['O']
            q.append((x // 2, step + 1, way_O))
            visited.add(x // 2)
for i in start_and_end:
    n, m = i[0], i[1]
    step, way = min_step(n, m)
    print(step)
    print(''.join(i for i in way))