n = int(input())
act = []
for i in range(n):
    start,end = map(int,input().split())
    act.append([start,end,end - start + 1])
act.sort(key = lambda x:x[1])
vac = [0 for _ in range(61)]
m = 0
for i in range(len(act)):
    if vac[act[i][0]:act[i][1]+1].count(1) == 0:
        vac[act[i][0]:act[i][1]+1] = [1 for i in range(act[i][2])] 
        m += 1
print(m)