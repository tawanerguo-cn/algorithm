n = int(input())
section = []
for _ in range(n):
    x1, y1 = map(int, input().split())
    section.append((x1, y1))
section.sort(key = lambda x: [x[1], -x[0]])
point = 0
last = float('-inf')
for i in range(n):
    if section[i][0] > last:
        point += 1
        last = section[i][1]
print(point)