n,q = map(int,input().split())
like = [[False for _ in range(n + 1)] for _ in range(n + 1)]
a = False
for i in range(q):
    x,y = map(int,input().split())
    like[x][y] = True
    for c in range(1,n + 1):
        if c != x and c != y and like[y][c] and like[c][x]:
            a = True
            break
if a:
    print('Yes')
else:
    print('No')