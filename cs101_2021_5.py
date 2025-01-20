n, m, l = map(int, input().split())
map_m = []
for _ in range(m):
    a1, b1 = map(int, input().split())
    map_m.append((a1, b1))
map_reverse = []
for i in map_m:
    map_1 = reversed(list(i))
    map_1 = tuple(map_1)
    map_reverse.append(map_1)
map_m.extend(map_reverse)
map_m = list(set(map_m))
map_m.sort(key = lambda x:(x[0], x[1]))
start = int(input())
def dls_range(n, m, l, map_m, start):
    visited = [False for _ in range(n)]
    visited_range = []
    visited_range.append(start)
    visited[start] = True
    def dfs(i, length):
        if length == l:
            return
        for j in map_m:
            if j[0] == i and not visited[j[1]]:
                visited[j[1]] = True
                visited_range.append(j[1])
                dfs(j[1], length + 1)
    dfs(start, 0)
    return visited_range
a = dls_range(n, m, l, map_m, start)
print(' '.join(str(i) for i in a))