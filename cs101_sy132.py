n = int(input())
list_n = [[] for _ in range(n)]
list_n[0] = '1'
for i in range(1,n):
    for m in range(len(list_n[i-1])):
        for j in range(i+1):
            list_n[i].append(list_n[i-1][m][:j] + f'{i+1}' + list_n[i-1][m][j:])
output = sorted([int(x) for x in list_n[n-1]])
for i in output:
    print(' '.join(str(i)))