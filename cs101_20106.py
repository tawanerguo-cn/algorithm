import heapq

def min_effort(m, n, terrain, test_cases):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n and terrain[x][y] != "#"
    def dijkstra(start, end):
        if terrain[start[0]][start[1]] == "#" or terrain[end[0]][end[1]] == "#":
            return "NO"
        heap = [(0, start[0], start[1])]
        visited = set()
        while heap:
            cost, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if (x, y) == end:
                return cost
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and (nx, ny) not in visited:
                    new_cost = cost + abs(int(terrain[nx][ny]) - int(terrain[x][y]))
                    heapq.heappush(heap, (new_cost, nx, ny))
        return "NO"
    results = []
    for start, end in test_cases:
        results.append(dijkstra(start, end))
    return results
m, n, p = map(int, input().split())
terrain = [input().split() for _ in range(m)]
test_cases = [tuple(map(int, input().split())) for _ in range(p)]
test_cases = [((x1, y1), (x2, y2)) for x1, y1, x2, y2 in test_cases]
results = min_effort(m, n, terrain, test_cases)
for res in results:
    print(res)

