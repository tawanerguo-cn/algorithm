d = int(input())
n = int(input())
rub = []
for _ in range(n):
    xi,yi,i1 = map(int,input().split())
    rub.append([xi + d,yi + d,i1])
boom_mat = [[0 for _ in range(1025 + 2 * d)] for _ in range(1025 + 2 * d)]
for k in rub:
    for i in range(-d,d + 1):
        for j in range(-d,d + 1):
            boom_mat[k[0] + i][k[1] + j] += k[2]
boom_set = set([boom_mat[i][j] for i in range (d,1025 + d) for j in range(d, 1025 + d)])
max_rub = max(list(boom_set))
m0 = 0
for i in range(d,1025 + d):
    for j in range(d,1025 + d):
        if boom_mat[i][j] == max_rub:
            m0 += 1
print(m0,max_rub)