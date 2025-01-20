from math import sqrt
#每个岛对应一个区间，本质上是多个区间问题
k = 1
while True:
    k += 1
    line = input().strip()
    if not line:
        continue#进入下一个循环
    n, d = map(int, line.split())
    if (n, d) == (0, 0):
        break
    island = []
    max_y = 0
    for _ in range(n):
        x1, y1 = map(int, input().split())
        max_y = max(max_y, y1)
        island.append((x1, y1))
    a = True
    if max_y > d:
        print(f'Case {k}: -1')
        a = False
    island_1 = []
    if a:
        for i in island:
            x_01, x_02 = i[0] - sqrt(d ** 2 - i[1] ** 2), i[0] + sqrt(d ** 2 - i[1] ** 2)
            island_1.append((x_01, x_02))
        island_1.sort(key = lambda x:(x[1], -x[1] + x[0]))
        d = 0
        radar = -float('inf')
        for i in island_1:
            if radar < i[0]:
                d += 1
                radar = i[1]
        print(f'Case {k}: {d}')
    
