m,n,p,q = map(int,input().split())
m1 = []
c = []
output = [[0 for _ in range(n + 1 - q)] for _ in range(m + 1 - p)]
for i in range(m):
    l1 = list(map(int,input().split()))
    m1.append(l1)
for i in range(p):
    l2 = list(map(int,input().split()))
    c.append(l2)
for i in range(m + 1 - p):
    for j in range(n + 1 - q):
        o = 0
        for k1 in range(p):
            for k2 in range(q):
                o += m1[i + k1][j + k2] * c[k1][k2]
        output[i][j] = o
for i in range(len(output)):
    print(' '.join(str(output[i][j]) for j in range(len(output[i]))))