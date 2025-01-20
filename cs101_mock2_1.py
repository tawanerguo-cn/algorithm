n = int(input())
p = []
for i in range(n):
    a,b = map(str,input().split())
    p.append([a,int(b)])
p1 = sorted(p,key = lambda x:x[1] ,reverse = True)
p2 = []
for i in range(len(p1)):
    if p1[i][1] >= 60:
        p2.append(p1[i][0])
for i in range(len(p2)):
    print(p2[i])
for i in range(len(p)):
    if p[i][1] < 60:
        print(p[i][0])
