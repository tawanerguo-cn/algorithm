n,k = map(int,input().split())
participants = list(map(int,input().split()))
m=0
for i in range(n):
    if participants[i]==0:
        break
    if i<k:
        m+=1
    if participants[i]==participants[k-1] and i>=k:
        m+=1
print(m)
