n = int(input())
a = [[0,0] for i in range(n)]
for i in range(n):
    a1,b1 = map(int,input().split())
    a[i][0] = a1
    a[i][1] = b1
list1 = sorted(a,key = lambda x:x[0])
list2 = sorted(a,key = lambda x:x[1])
if list1 == list2:
    print('Poor Alex')
else:
    print('Happy Alex')