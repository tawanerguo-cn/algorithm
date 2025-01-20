matrix=[]
for i in range(5):
    matrix.append(list(map(int,input().split())))
    if matrix[i].count(1)!=0:
        m=i
        n=matrix[i].index(1)
print(abs(m-2)+abs(n-2))