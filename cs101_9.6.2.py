n = int(input())
essay = list(map(str,input().split()))
count = 0
m = 0
list_index = [0]
for i in range(n):
    count += len(essay[i])+1
    if count > 81:
        count = len(essay[i])+1
        list_index.append(i)
list_index.append(n)
for i in range(len(list_index)-1):
    print(' '.join(essay[j] for j in range(list_index[i],list_index[i+1])))