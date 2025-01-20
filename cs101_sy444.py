n = int(input())
section = []
for _ in range(n):
    x1, y1 = map(int, input().split())
    section.append((x1, y1))
section.sort(key = lambda x: x[1])
m = 1
last = section[0][1]
for i in range(1, n):
    if section[i][0] >= last:
        m += 1
        last = section[i][1]
print(m)
