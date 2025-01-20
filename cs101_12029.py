import sys
from collections import deque

dx=[0,1,0,-1]
dy=[-1,0,1,0]
input = sys.stdin.read
a=input().split()
idx=0
k=int(a[idx])
idx+=1
ans=[]
for _ in range(k):
    m,n=map(int,a[idx:idx+2])
    idx+=2
    h=[]
    hw=[[0 for i in range(n)]for j in range(m)]
    for i in range(m):
        h.append(list(map(int,a[idx:idx+n])))
        idx+=n
    tx,ty=map(int,a[idx:idx+2])
    tx,ty=tx-1,ty-1
    idx+=2
    p=int(a[idx])
    idx+=1
    for i in range(p):
        x,y=map(int,a[idx:idx+2])
        idx+=2
        x,y=x-1,y-1
        q=deque()
        q.append((x,y))
        if h[x][y]<=h[tx][ty]:
            continue
        ht=h[x][y]
        hw[x][y]=h[x][y]
        while q:
            x,y=q.popleft()
            for j in range(4):
                nx,ny=x+dx[j],y+dy[j]
                if 0<=nx<m and 0<=ny<n:
                    if ht>hw[nx][ny] and ht>h[nx][ny]:
                        hw[nx][ny]=ht
                        q.append((nx,ny))
    ans.append('Yes' if hw[tx][ty]>0 else 'No')
sys.stdout.write('\n'.join(ans)+'\n')