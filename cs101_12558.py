n,m = map(int,input().split())
map1 = [[0 for _ in range(m + 2)]]
for _ in range(n):
    l1 = [0]
    l1.extend(list(map(int,input().split())))
    l1.extend([0])
    map1.append(l1)
map1.append([0 for _ in range(m + 2)])
p = 0
for i in range(1,n + 1):
    for j in range(1,m + 1):
        if map1[i][j] == 1:
            if [map1[i-1][j],map1[i + 1][j],map1[i][j-1],map1[i][j + 1]].count(0) == 1:
                p += 1
            elif [map1[i-1][j],map1[i + 1][j],map1[i][j-1],map1[i][j + 1]].count(0) == 2:
                p += 2
            elif [map1[i-1][j],map1[i + 1][j],map1[i][j-1],map1[i][j + 1]].count(0) == 3:
                p += 3
            elif [map1[i-1][j],map1[i + 1][j],map1[i][j-1],map1[i][j + 1]].count(0) == 4:
                p += 4
print(p)