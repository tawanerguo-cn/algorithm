n,m = map(int,input().split())
m1 = []
for i in range(n):
    r1 = list(map(int,input().split()))
    m1.append(r1)
num = []
for i in range(n):
    for j in range(m):
        x = m1[i][j]
        a,b,c,d = m1[0][j],m1[i][m-1],m1[n-1][j],m1[i][0]
        n1 = int(''.join(str(i) for i in [a,b,c,d]))
        num.append(n1 * x)
print(max(num))