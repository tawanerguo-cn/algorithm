from math import sqrt
case_number = 1
while True:
    line = input().strip()
    if not line:
        continue
    n, d = map(float, line.split())
    n = int(n)
    if n == 0:
        break
    x, y = [], []
    for _ in range(n):
        xi, yi = map(float, input().split())
        x.append(xi)
        y.append(yi)
    if max(y) > d:
        print(f'Case {case_number}: -1')
    else:
        x_c = []
        r = 0
        for i in range(n):
            x_c.append([x[i] - sqrt(d ** 2 - y[i] ** 2), x[i] + sqrt(d ** 2 - y[i] ** 2)])
        x_c.sort(key=lambda x: x[1])
        end = -float('inf')
        for interval in x_c:
            if interval[0] > end:
                r += 1
                end = interval[1]
        print(f'Case {case_number}: {r}')
    case_number += 1
