h = int(input())
m = int(input())
sc = []
for _ in range(m):
    s,c = map(float,input().split())
    sc.append([s,c,s * c])
t = 2 * h - 0.5 * m
sc.sort(key = lambda x:(-x[2]))
i = 0
score = 0
while i < m:
    if t >= 5 / sc[i][0]:
        score += 5 * sc[i][1]
        t -= 5 / sc[i][0]
        i += 1
    else:
        score += (t * sc[i][0]) * sc[i][1]
        break
print(f'{score:.1f}')