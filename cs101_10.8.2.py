n,q = map(int,input().split())
like = []
like1 = []
for i in range(q):
    x,y = map(int,input().split())
    like.append([x,y])
    like1.append([y,x])
m = 0
for i in like1:
    if i in like:
        m += 1
if m != 0:
    print('Yes')
else:
    print('No')
